# fsl_sub python module
# Copyright (c) 2018-2020, University of Oxford (Duncan Mortimer)

import datetime
import errno
import importlib
from importlib.resources import files
import json
import logging
import math
import os
import pkgutil
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from functools import lru_cache
from math import ceil
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml import YAML

from fsl_sub.exceptions import (
    CommandError,
    BadOS,
    BadSubmission,
    BadConfiguration,
    InstallError,
    NotAFslDir,
    NoCondaEnv,
    NoCondaEnvFile,
    NoFsl,
    PackageError,
    UpdateError,
)
from fsl_sub.system import (
    system_stdout,
)
from fsl_sub.version import VERSION
from shutil import which


def even(n):
    '''Rounds number up to nearest even

    >>> even(1)
    2
    >>> even(2)
    2
    >>> even(7)
    8
    '''
    return n + (n % 2)


def smt_threads(t, queue_def):
    '''Ensure threads are next highest even number if smt is true

    >>> smt_threads(3, {})
    3
    >>> smt_threads(4, {})
    4
    >>> smt_threads(1, {'smt': True, })
    2
    >>> smt_threads(5, {'smt': False, })
    5
    >>> smt_threads(2, {'smt': True, })
    2
    >>> smt_threads(2, {'smt': False, })
    2
    '''
    if queue_def:
        if queue_def.get('smt', False):
            t = even(t)
    return t


def command_exists(command, ctype='command', usescript=False):
    if ctype == 'array':
        try:
            check_command_file(command)
        except CommandError as e:
            raise BadSubmission(
                "Array task definition file fault: " + str(e)
            )
    elif ctype == 'command':
        if usescript is False:
            try:
                check_command(command)
            except CommandError as e:
                raise BadSubmission(
                    "Command not usable: " + str(e)
                )
        else:
            if not os.path.exists(command):
                raise BadSubmission(
                    "Script file not found"
                )
    else:
        raise BadConfiguration(
            "Unknown validation type: " + ctype)


def make_logdir(logdir=None):
    if logdir is None or logdir == "/dev/null":
        return
    try:
        os.makedirs(logdir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise BadSubmission(
                "Unable to create {0} ({1})".format(
                    logdir, str(e)
                ))
        else:
            if not os.path.isdir(logdir):
                raise BadSubmission(
                    "Log destination is a file "
                    "(should be a folder)")


def bash_cmd():
    '''Where is a 'sh' shell? Bash on Linux or ZSH on modern macOS'''

    if 'FSLSUB_SHELL' in os.environ:
        return os.environ['FSLSUB_SHELL']

    if (platform.system() == 'Darwin'
            and int(platform.uname()[2].split('.')[0]) > 18):
        bash = which('zsh')
    else:
        bash = which('bash')
    if bash is None:
        raise BadOS("Unable to find BASH")
    return bash


@lru_cache()
def load_plugins(skip_mydir=False):
    plugin_path = []
    if not skip_mydir:
        if 'FSLSUB_PLUGINPATH' in os.environ:
            plugin_path.extend(os.environ['FSLSUB_PLUGINPATH'].split(':'))
        here = files('fsl_sub')
        plugin_path.append(str(here.joinpath('plugins')))

    sys_path = sys.path
    ppath = list(plugin_path)
    ppath.reverse()
    for p_dir in ppath:
        sys.path.insert(0, p_dir)

    plugin_dict = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('fsl_sub_plugin')
    }
    sys.path = sys_path
    return plugin_dict


def available_plugins():
    PLUGINS = load_plugins()

    plugs = []
    for p in PLUGINS.keys():
        (_, plugin_name) = p.split('plugin_')
        plugs.append(plugin_name)

    return plugs


def get_plugin_versions(plugins):
    p_versions = []
    for plugin in plugins.keys():
        try:
            plugin_version = plugins[plugin].plugin_version()
        except AttributeError as e:
            raise BadConfiguration(
                "Failed to load plugin " + plugin
                + " ({0})".format(str(e))
            )
        p_versions.append((plugin, plugin_version))
    return p_versions


def get_plugin_default_conf(plugin_name):
    PLUGINS = load_plugins()
    grid_module = 'fsl_sub_plugin_' + plugin_name

    if grid_module not in PLUGINS:
        raise CommandError("Plugin {} not found". format(plugin_name))

    try:
        return PLUGINS[grid_module].default_conf()
    except AttributeError:
        raise BadConfiguration(
            "Plugin doesn't provide a default configuration."
        )


def plugins_provide_coproc(methods):
    PLUGINS = load_plugins()
    for plugin_name in methods:
        grid_module = 'fsl_sub_plugin_' + plugin_name
        try:
            if PLUGINS[grid_module].provides_coproc_config():
                return True
        except KeyError:
            pass
    return False


def get_plugin_queue_defs(plugin_name):
    PLUGINS = load_plugins()
    grid_module = 'fsl_sub_plugin_' + plugin_name

    if grid_module not in PLUGINS:
        raise CommandError("Plugin {} not found". format(plugin_name))

    try:
        return PLUGINS[grid_module].build_queue_defs()
    except AttributeError:
        return ''


def get_plugin_already_queued(plugin_name):
    PLUGINS = load_plugins()
    grid_module = 'fsl_sub_plugin_' + plugin_name

    if grid_module not in PLUGINS:
        raise CommandError("Plugin {} not found". format(plugin_name))

    try:
        return PLUGINS[grid_module].already_queued()
    except AttributeError:
        return False


def get_plugin_qdel(plugin_name):
    PLUGINS = load_plugins()
    grid_module = 'fsl_sub_plugin_' + plugin_name

    if grid_module not in PLUGINS:
        raise CommandError("Plugin {} not found". format(plugin_name))

    try:
        return PLUGINS[grid_module].qdel
    except AttributeError as e:
        raise CommandError from e


def minutes_to_human(minutes):
    if minutes < 60:
        result = "{}m".format(minutes)
    elif minutes < 60 * 24:
        result = "{:.1f}".format(minutes / 60)
        (a, b) = result.split('.')
        if b == '0':
            result = a
        result += 'h'
    else:
        result = "{:.1f}".format(minutes / (60 * 24))
        (a, b) = result.split('.')
        if b == '0':
            result = a
        result += 'd'
    return result


def titlize_key(text):
    '''Remove _ and Title case a dict key'''

    return text.replace('_', ' ').title()


def blank_none(text):
    '''Return textual value or blank if value is None'''

    if text is None:
        return ''
    else:
        return str(text)


def human_to_ram(ram, output='M', units='G', as_int=True, round_down=False):
    '''Converts user supplied RAM quantity into output scale'''
    scale_factors = {
        'P': 50,
        'T': 40,
        'G': 30,
        'M': 20,
        'K': 10,
        'B': 0
    }
    try:
        units = units.upper()
        output = output.upper()
    except AttributeError:
        raise ValueError("units and output must be strings")
    if units not in scale_factors or output not in scale_factors:
        raise ValueError('Unrecognised RAM multiplier')
    if isinstance(ram, (int, float)):
        ram = str(ram) + units
    if not isinstance(ram, str):
        raise ValueError('Unrecognised RAM string')
    try:
        if '.' in ram:
            float(ram)
        else:
            int(ram)
    except ValueError:
        pass
    else:
        ram = ram + units
    regex = r'(?P<ram>[\d.]+)(?P<units>[GgMmKkTtPp])[iI]?[bB]?'
    h_ram = re.match(regex, ram)
    if h_ram is None:
        raise ValueError("Supplied memory doesn't look right")
    match = h_ram.groupdict()
    units = match['units'].upper()
    try:
        if '.' in match['ram']:
            ram = float(match['ram'])
        else:
            ram = int(match['ram'])
    except ValueError:
        raise ValueError("RAM amount not a valid number")
    size = (
        ram * 2 ** scale_factors[units]
        / 2 ** scale_factors[output])
    if as_int:
        if round_down:
            size = int(math.floor(size))
        else:
            size = int(math.ceil(size))
    return size


def affirmative(astring):
    '''Is the given string a pseudonym for yes'''
    answer = astring.lower()
    if answer == 'yes' or answer == 'y' or answer == 'true':
        return True
    else:
        return False


def negative(astring):
    '''Is the given string a pseudonym for no'''
    answer = astring.lower()
    if answer == 'no' or answer == 'n' or answer == 'false':
        return True
    else:
        return False


def truthy(value):
    '''Is the value representative of true or false?'''

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        text = value.lower()

        if text == '1' or text == 'true':
            return True
        elif text == '0' or text == 'false':
            return False

        return False

    elif isinstance(value, int):
        return not value == 0

    else:
        raise ValueError("Not truthy type")


def check_command(cmd):
    if shutil.which(cmd) is None:
        raise CommandError("Cannot find script/binary '{}'".format(cmd))


def check_command_file(cmds):
    try:
        with open(cmds, 'r') as cmd_file:
            for lineno, line in enumerate(cmd_file.readlines()):
                line = line.strip()
                if line == '':
                    raise CommandError(
                        "Array task file contains a blank line at line " +
                        str(lineno + 1))
                if line.startswith('#'):
                    raise CommandError(
                        "Array task file contains comment line (begins #) " +
                        "at line " + str(lineno + 1))
                cmd = shlex.split(line)[0].rstrip(';')
                if cmd == 'dummy':
                    # FEAT creates an array task file that contains
                    # the line 'dummy' as a previous queued task will
                    # have populated this file with the real command(s)
                    # by the time this command file is actually used
                    continue
                try:
                    check_command(cmd)
                except CommandError:
                    raise CommandError(
                        "Cannot find script/binary {0} on line {1}"
                        " of {2}".format(cmd, lineno + 1, cmd_file.name))
    except (IOError, FileNotFoundError):
        raise CommandError("Unable to read '{}'".format(cmds))


def control_threads(env_vars, threads, env_dict=None, add_to_list=None):
    '''Set the specified environment variables to the number of
    threads.'''
    if isinstance(threads, int):
        st = str(threads)
    if 'FSLSUB_PARALLEL' not in env_vars:
        env_vars.append('FSLSUB_PARALLEL')

    for ev in env_vars:
        if env_dict is None:
            os.environ[ev] = st
        else:
            env_dict[ev] = st

        export_item = '='.join((ev, st))
        if add_to_list is not None:
            update_envvar_list(add_to_list, export_item)


def update_envvar_list(envlist, variable, overwrite=True):
    '''Updates envlist (['VAR', 'VAR2=VALUE', ]) to include variable
    (variable string can contain =VALUE) will ensure no duplicates
    or multiple setting of same variable to different values.
    If overwrite is True will overwrite existing value in envlist,
    otherwise will only add missing variables.'''
    if len(envlist) == 0:
        envlist.append(variable)
        return
    # Remove any =...
    var = variable.split('=')[0]

    found = False
    for index, lvar in enumerate(envlist):
        if '=' in lvar:
            lvar = lvar.split('=')[0]
        if lvar == var:
            found = True
            if overwrite:
                envlist.pop(index)
    if (found and overwrite) or not found:
        envlist.append(variable)


def split_ram_by_slots(jram, jslots):
    return int(ceil(jram / jslots))


def file_is_image(filename):
    '''Is the specified file an image file?'''
    if os.path.isfile(filename):
        try:
            if system_stdout(
                command=[
                    os.path.join(
                        os.environ['FSLDIR'],
                        'bin',
                        'imtest'),
                    filename
                ]
            )[0] == '1':
                return True
        except KeyError:
            raise NoFsl(
                "FSLDIR environment variable not found")
        except subprocess.CalledProcessError as e:
            raise CommandError(
                "Error trying to check image file - "
                + str(e))
    return False


def parse_array_specifier(spec):
    if ':' in spec:
        (jrange, step) = spec.split(':')
        try:
            step = int(step)
        except ValueError:
            raise BadSubmission("Array step must be an integer")
    else:
        step = None
        jrange = spec
    if '-' in jrange:
        (jstart, jend) = jrange.split("-")
        try:
            jstart = int(jstart)
        except ValueError:
            raise BadSubmission("Array start index must be an integer")
        try:
            jend = int(jend)
        except ValueError:
            raise BadSubmission("Array end index must be an integer")
    else:
        jstart = spec
        try:
            jstart = int(jstart)
        except ValueError:
            raise BadSubmission("Array number of tasks must be an integer")
        jend = None
    return (jstart, jend, step)


def user_input(prompt):
    return input(prompt)


@lru_cache()
def find_fsldir(prompt=True):
    fsldir = None
    try:
        fsldir = os.environ['FSLDIR']
    except KeyError:
        while fsldir is None and prompt:
            fsldir = user_input(
                "Where is FSL installed? (hit return if FSL not installed) ")
            if fsldir == "":
                raise NotAFslDir()
            if not os.path.exists(
                    os.path.join(fsldir, 'etc', 'fslconf')):
                print("Not an FSL dir.", file=sys.stderr)
                fsldir = None
    return fsldir


@lru_cache()
def get_fslversion():
    """Returns the FSL version (as read from $FSLDIR/etc/fslversion)
    as a tuple of integers.
    """
    fsldir = find_fsldir()
    if fsldir is None:
        raise NotAFslDir()
    fslverfile = os.path.join(fsldir, 'etc', 'fslversion')
    if not os.path.exists(fslverfile):
        raise NotAFslDir()

    with open(fslverfile, 'rt') as f:
        contents = f.read()
    # FSL <= 6.0.5 contains a fsl/FslBuildManifests
    # commit hash after the version string, separated
    # by a colon
    parts = contents.split(':')[0].split('.')
    # FSL >=6.0.6 may have non-integer trailing components
    # (fsl/conda/manifest commit hash, branch name)
    fslversion = []
    for part in parts:
        try:
            fslversion.append(int(part))
        except Exception:
            break
    return tuple(fslversion)


def conda_fsl_env(fsldir=None):
    try:
        if fsldir is None:
            fsldir = find_fsldir()
    except NotAFslDir:
        raise NoCondaEnv("Not installed in FSL - install/update not supported")
    else:
        env_dir = os.path.join(fsldir, 'fslpython', 'envs', 'fslpython')
    if not os.path.exists(env_dir):
        raise NoCondaEnv("FSL Conda environment folder doesn't exist")
    return env_dir


def conda_bin(fsldir=None):
    try:
        fsl_env = conda_fsl_env(fsldir)
    except NoCondaEnv:
        conda_bin = None
    else:
        if fsl_env is not None:
            conda_bin = os.path.join(fsl_env, '..', '..', 'bin', 'conda')
            if not (
                    os.path.exists(conda_bin)
                    and os.access(conda_bin, os.X_OK)):
                conda_bin = None
        else:
            conda_bin = shutil.which('conda')

    if conda_bin is None:
        raise NoCondaEnv("Unable to find 'conda' in FSL")
    return conda_bin


def conda_channels(fsldir=None):
    channels = []
    yaml = YAML(typ='safe')
    if fsldir is None:
        fsldir = find_fsldir(fsldir)
    if fsldir is not None:
        try:
            with open(
                    os.path.join(
                        fsldir,
                        'etc',
                        'fslconf',
                        'fslpython_environment.yml'),
                    "r") as fsl_pyenv:
                conda_env = yaml.load(fsl_pyenv)

        except Exception as e:
            raise NoCondaEnvFile(
                "Unable to access fslpython_environment.yml file: "
                + str(e))
        try:
            channels = conda_env['channels']
        except KeyError:
            pass
    return channels


def conda_stderr(output):
    '''Finds the actual error in the stderr output of conda --json
    This is often poluted with messages of no interest.'''
    json_lines = []
    json_found = False
    for line in output.splitlines():
        if line.startswith('sl_{') or line.startswith('{'):
            json_found = True
        if json_found:
            if line.startswith('sl_'):
                line = line.replace('sl_', '')
            if line.startswith('}'):
                json_lines.append('}')
                json_found = False
            else:
                json_lines.append(line)
    if json_lines:
        try:
            message_obj = json.loads('\n'.join(json_lines))
        except json.JSONDecodeError:
            message = None
            for line in output.splitlines():
                line = line.strip()
                if line.strip().strip('"').startswith('message'):
                    message = line.split(':')[1].strip().strip('"')
            if message is not None:
                message_obj = {'message': message, }
            else:
                message_obj = {'message': output, }
    else:
        message_obj = {'message': output, }
    try:
        message = message_obj['message']
    except KeyError:
        return output
    return message


def conda_stdout_error(output):
    '''Return the error message in stdout of conda --json'''
    try:
        message_obj = json.loads(output)
        message = message_obj['message']
    except (json.JSONDecodeError, KeyError):
        message = output
    return message


def conda_json(command, options, with_channel=True):
    if isinstance(options, str):
        options = [options, ]
    try:
        cb = conda_bin()
    except NoCondaEnv as e:
        raise PackageError(e)

    channels = []
    if with_channel:
        try:
            channels = conda_channels()
        except NoCondaEnvFile as e:
            raise PackageError(
                "FSL lacks Python distribution: {0}. ".format(str(e)))

    cmd_line = [cb, command, '--json', ]
    for channel in channels:
        cmd_line.extend(['-c', channel, ])
    cmd_line.extend(options)

    try:
        result = subprocess.run(
            cmd_line,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            universal_newlines=True
        )
    except subprocess.CalledProcessError as e:
        if e.stderr is None:
            message = conda_stdout_error(e.output)
        else:
            message = e.stderr
        raise PackageError(message)

    conda_json = result.stdout
    try:
        conda_result = json.loads(conda_json)
    except json.JSONDecodeError as e:
        raise PackageError(str(e))

    return conda_result


def conda_find_packages(match, fsldir=None):
    if isinstance(match, str):
        match = [match, ]
    if not conda_pkg_dirs_writeable(fsldir):
        raise PackageError(
            "No permission to change Conda environment folder, re-try with "
            "'sudo --preserve-env=FSLDIR fsl_sub_plugin -l'.")

    try:
        conda_result = conda_json('search', match)
    except PackageError as e:
        raise PackageError(
            "Unable to search for packages! ({0})".format(e))

    return list(conda_result.keys())


def conda_pkg_dirs_writeable(fsldir=None):
    if fsldir is None:
        fsldir = find_fsldir()
    try:
        conda_result = conda_json('info', [], with_channel=False)
    except PackageError as e:
        raise PackageError("Unable to check for updates ({0})".format(str(e)))

    for pdir in conda_result['pkgs_dirs']:
        if pdir.startswith(fsldir):
            if not os.access(pdir, os.W_OK):
                return False

    return True


def get_conda_packages(conda_env):
    # Get list of packages installed in environment
    args = [
        '-q',
        '-p',
        conda_env,
    ]

    try:
        conda_result = conda_json('list', args, with_channel=False)
    except PackageError as e:
        raise PackageError(
            "Unable to get package listing ({0})".format(str(e)))

    return [a['name'] for a in conda_result if a['name'].startswith('fsl_sub')]


def conda_check_update(fsldir=None):
    try:
        conda_env = conda_fsl_env(fsldir)
    except NoCondaEnv as e:
        raise PackageError("Unable to check for updates ({0})".format(str(e)))

    if not conda_pkg_dirs_writeable(fsldir):
        raise PackageError(
            "No permission to change Conda environment folder, re-try with "
            "'sudo --preserve-env=FSLDIR fsl_sub_update -c'.")

    try:
        packages = get_conda_packages(conda_env)
    except PackageError as e:
        raise UpdateError(e)

    if not packages:
        raise PackageError("No fsl_sub packages installed")

    args = [
        '-q',
        '-p',
        conda_env,
        '--dry-run',
    ]
    args.extend(packages)
    try:
        conda_result = conda_json('update', args)
    except PackageError as e:
        raise UpdateError("Unable to check for updates ({0})".format(str(e)))

    updates = None
    try:
        try:
            if conda_result['message'] == (
                    'All requested packages already installed.'):
                return None
        except KeyError:
            pass
        to_link = conda_result['actions']['LINK']
        updates = {
            a['name']: {
                'version': a['version'], } for a in
            to_link
        }
        to_unlink = conda_result['actions']['UNLINK']
        old_versions = {
            a['name']: a['version'] for a in
            to_unlink
        }
        for pkg in updates.keys():
            try:
                updates[pkg]['old_version'] = old_versions[pkg]
            except KeyError:
                pass
    except KeyError as e:
        raise UpdateError(
            "Unexpected update output ({0})".format(str(e))
        )
    return updates


def conda_update(fsldir=None):
    try:
        conda_env = conda_fsl_env(fsldir)
    except NoCondaEnv as e:
        raise UpdateError("Unable to update! ({0})".format(str(e)))

    if not conda_pkg_dirs_writeable(fsldir):
        raise UpdateError(
            "No permission to change Conda environment folder, re-try with "
            "'sudo --preserve-env=FSLDIR fsl_sub_update'.")

    try:
        packages = get_conda_packages(conda_env)
    except PackageError as e:
        raise UpdateError(e)

    args = [
        '-q',
        '-y',
        '-p',
        conda_env,
    ]
    args.extend(packages)
    try:
        conda_result = conda_json('update', args)
    except PackageError as e:
        raise UpdateError("Unable to update! ({0})".format(str(e)))

    try:
        try:
            if conda_result['message'] == (
                    'All requested packages already installed.'):
                return None
        except KeyError:
            pass
        if not conda_result['success']:
            raise UpdateError(conda_result['message'])
        to_link = conda_result['actions']['LINK']
        updates = {
            a['name']: {
                'version': a['version'], } for a in
            to_link
        }
        to_unlink = conda_result['actions']['UNLINK']
        old_versions = {
            a['name']: a['version'] for a in
            to_unlink
        }
        for pkg in updates.keys():
            try:
                updates[pkg]['old_version'] = old_versions[pkg]
            except KeyError:
                pass
        return updates

    except KeyError as e:
        raise UpdateError(
            "Unexpected update output ({0})".format(str(e))
        )


def conda_install(packages, fsldir=None):
    if isinstance(packages, str):
        packages = (packages, )

    try:
        conda_env = conda_fsl_env(fsldir)
    except NoCondaEnv as e:
        raise InstallError("Unable to install ({0})".format(str(e)))

    if not conda_pkg_dirs_writeable(fsldir):
        raise InstallError(
            "No permission to change Conda environment folder, " +
            "re-try with 'sudo'.")

    args = [
        '-q',
        '-y',
        '-p',
        conda_env,
    ]
    args.extend(packages)

    try:
        conda_result = conda_json('install', args)
    except PackageError as e:
        raise InstallError("Unable to install! ({0})".format(e))

    try:
        if ('message' in conda_result
            and conda_result['message']
                == 'All requested packages already installed.'):
            return None
        if not conda_result['success']:
            raise InstallError(
                "Unable to install ({0})".format(
                    conda_result['message']
                )
            )
        to_link = conda_result['actions']['LINK']
        updates = {
            a['name']: {
                'version': a['version'], } for a in
            to_link
        }
        return updates

    except KeyError as e:
        raise InstallError(
            "Unexpected update output - {0} missing".format(str(e))
        )


def flatten_list(args):
    flattened = []
    for item in args:
        if isinstance(item, list):
            flattened.extend([i for i in item])
        else:
            flattened.append(item)
    return flattened


def fix_permissions(fname, mode):
    '''Change permissions on fname, honouring umask.
    Mode should be octal number'''
    umask = os.umask(0)
    os.umask(umask)
    new_mode = mode & ~umask
    os.chmod(fname, new_mode)


def listplusnl(li):
    for i in li:
        yield i
        yield '\n'


def writelines_nl(fh, lines):
    '''Takes a file handle and a list of lines (sans newline) to write out,
    adding newlines'''
    fh.writelines(listplusnl(lines))


def job_script(
        command, command_args, q_prefix, q_plugin,
        modules=None, extra_lines=None, modules_paths=None):
    '''Build a job script for 'command' with arguments 'command_args'.
    q_prefix is prefix to add to queue command lines,
    q_plugin is a tuple (plugin short name, plugin_version)
    modules is a list of shell modules to load and extra_lines will be added
    between the header and the command line'''

    if modules_paths is None:
        modules_paths = []
    if modules is None:
        modules = []
    if extra_lines is None:
        extra_lines = []
    logger = logging.getLogger('fsl_sub.fsl_sub_plugin_' + q_plugin[0])
    bash = bash_cmd()

    job_def = ['#!' + bash, '', ]
    for cmd in command_args:
        if type(cmd) is list:
            cmd = [str(c) for c in cmd]
            job_def.append(' '.join((q_prefix, ' '.join(cmd))))
        else:
            job_def.append(' '.join((q_prefix, str(cmd))))

    logger.debug("Creating module load lines")
    logger.debug("Adding modules paths")
    if modules_paths:
        mpaths = list(modules_paths)
        mpaths.append('$MODULEPATH')
        job_def.append('MODULEPATH=' + ':'.join(mpaths))
    logger.debug("Module list is " + str(modules))
    for module in modules:
        job_def.append("module load " + module)

    job_def.append(
        "# Built by fsl_sub v.{0} and fsl_sub_plugin_{1} v.{2}".format(
            VERSION, q_plugin[0], q_plugin[1]
        ))
    job_def.append("# Command line: " + " ".join(sys.argv))
    job_def.append(
        "# Submission time (H:M:S DD/MM/YYYY): " +
        datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"))
    job_def.append('')
    job_def.extend(extra_lines)
    if type(command) is list:
        job_def.append(" ".join(command))
    else:
        job_def.append(command)
    job_def.append('')
    return job_def


def write_wrapper(content):
    with tempfile.NamedTemporaryFile(
            mode='wt',
            delete=False) as wrapper:
        writelines_nl(wrapper, content)

    return wrapper.name


def merge_dict(base_dict, addition_dict):
    for k, v in base_dict.items():
        if k in addition_dict:
            if isinstance(addition_dict[k], dict):
                addition_dict[k] = merge_dict(v, addition_dict[k])
    new_dict = base_dict.copy()
    new_dict.update(addition_dict)
    return new_dict


def merge_commentedmap(d, n):
    '''Merge ruamel.yaml round-trip dict-a-likes'''
    if isinstance(n, CommentedMap):
        for k in n:
            d[k] = merge_commentedmap(d[k], n[k]) if k in d else n[k]
            if k in n.ca._items and n.ca._items[k][2] and \
                    n.ca._items[k][2].value.strip():
                d.ca._items[k] = n.ca._items[k]  # copy non-empty comment
    else:
        d = n
    return d


def yaml_repr_none(self, data):
    return self.represent_scalar('tag:yaml.org,2002:null', 'Null')


def build_job_name(command):
    '''Return a name for the job'''

    if isinstance(command, list):
        command = command[0]
    # Remove quotes, split on any ';', take the last item, remove
    # surrounding spaces and split on space
    return os.path.basename(
        command.strip('"').strip("'").split(';')[-1].strip().split()[0])
