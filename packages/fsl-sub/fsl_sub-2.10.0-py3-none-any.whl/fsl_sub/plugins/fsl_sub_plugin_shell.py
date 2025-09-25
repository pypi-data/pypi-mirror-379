# fsl_sub python module
# Copyright (c) 2018-2021, University of Oxford (Duncan Mortimer)

# fsl_sub plugin for running directly on this computer
import datetime
from importlib.resources import files
import logging
from multiprocessing import get_context
import os
import shlex
import subprocess as sp
import sys
import warnings

from fsl_sub.config import (
    method_config,
    read_config,
)
from fsl_sub.exceptions import (
    BadSubmission,
    MissingConfiguration,
    UnrecognisedModule,
    ShellBadSubmission, )
from fsl_sub.shell_modules import (loaded_modules, load_module, )
from fsl_sub.utils import (
    bash_cmd,
    parse_array_specifier,
    writelines_nl,
    control_threads,
)
from fsl_sub.version import VERSION
from collections import defaultdict


def plugin_version():
    return '2.0.2'


def qtest():
    '''Command that confirms method is available'''
    return True


def queue_exists(qname, qtest=qtest()):
    '''Command that confirms a queue is available'''
    return True


def already_queued():
    '''Is this a running in a submitted job?'''
    return False


def qdel(job_id):
    '''Not supported for shell running'''
    warnings.warn("Not supported - use kill -HUP " + str(job_id))
    return ("", 0)


def build_queue_defs():
    return ''


def _disable_parallel(job):
    mconf = defaultdict(lambda: False, method_config('shell'))

    matches = mconf['parallel_disable_matches']

    job_dir = os.path.dirname(job)
    if job_dir == '.':
        job_dir = ''
    job_cmd = os.path.basename(job)
    if matches:
        for m in matches:
            m_dir = os.path.dirname(m)
            m_cmd = os.path.basename(m)
            m_cmd_no_wc = m_cmd.strip('*')

            if m_dir and job_dir != m_dir:
                return False
            if job_dir and m_dir and job_dir != m_dir:
                return False
            if (
                    m_cmd.startswith('*')
                    and job_cmd != m_cmd_no_wc
                    and job_cmd.endswith(m_cmd_no_wc)):
                return True
            if (
                    m_cmd.endswith('*')
                    and job_cmd != m_cmd_no_wc
                    and job_cmd.startswith(m_cmd_no_wc)):
                return True
            if job_cmd == m_cmd:
                return True
    return False


def _get_logger():
    return logging.getLogger('fsl_sub.' + __name__)


def _to_file():
    return method_config('shell').get('log_to_file', False)


def submit(
        command,
        job_name,
        threads=None,
        queue=None,
        array_task=False,
        array_limit=None,
        array_specifier=None,
        logdir=None,
        keep_jobscript=None,
        coprocessor=None,
        coprocessor_toolkit=None,
        export_vars=None,
        **kwargs):
    '''Submits the job'''
    logger = _get_logger()
    logger.debug(
        ",".join((
            str(command),
            job_name,
            str(threads),
            str(queue),
            str(array_task),
            str(array_limit),
            str(array_specifier),
            str(logdir),
            str(keep_jobscript),
            str(coprocessor),
            str(coprocessor_toolkit),
            str(export_vars),
            str(kwargs),
        )))
    mconf = defaultdict(lambda: False, method_config('shell'))
    jobid_var = None
    taskid_var = None

    jid = os.getpid()

    if command is None:
        raise BadSubmission(
            "Must provide command line or array task file name")
    if not isinstance(command, list):
        raise BadSubmission(
            "Internal error: command argument must be a list"
        )
    if export_vars is None:
        export_vars = []

    # Look for passing one-line complex shell commands
    if (
            ';' in ' '.join(command)
            or '|' in ' '.join(command)
            or '>' in ' '.join(command)):
        command = [bash_cmd(), '-c', ' '.join(command), ]

    set_vars = dict(var.split('=', 1) for var in export_vars if '=' in var)

    if keep_jobscript is None:
        keep_jobscript = mconf.get('keep_jobscript', False)
    logger.debug("Requested job script is kept? %s" % keep_jobscript)

    logger.debug("Looking for parent job id(s)")
    jobid_var = None
    taskid_var = None

    try:
        jobid_var = os.environ['FSLSUB_JOBID_VAR']
        taskid_var = os.environ['FSLSUB_ARRAYTASKID_VAR']
    except KeyError:
        pass

    logger.debug(f"Requested threads: {threads}")
    if threads is None and 'FSLSUB_PARALLEL' not in os.environ:
        logger.debug("Defining FSLSUB_PARALLEL to be 0")
        os.environ['FSLSUB_PARALLEL'] = '0'
    if jobid_var is not None:
        logger.debug("Getting job ids from environment")
        task_id = None
        task_subjid = None
        try:
            task_id = os.environ[jobid_var]
        except KeyError:
            raise BadSubmission(
                "FSLSUB_JOBID_VAR points to a non-existant variable!")
        if taskid_var is not None:
            try:
                task_subjid = os.environ[taskid_var]
            except KeyError:
                raise BadSubmission(
                    'FSLSUB_ARRAYTASKID_VAR points to a non-existant '
                    'variable!')
        if task_subjid is not None and task_subjid != 'undefined':
            task_id = '.'.join((task_id, task_subjid))
        log_jid = '-'.join((task_id, str(jid)))
    else:
        log_jid = str(jid)

    if logdir is None:
        logger.debug("Setting logdir to current directory")
        logdir = os.getcwd()
    logfile_base = os.path.join(logdir, job_name)
    stdout = "{0}.{1}{2}".format(logfile_base, 'o', log_jid)
    stderr = "{0}.{1}{2}".format(logfile_base, 'e', log_jid)
    logger.debug("stdout > %s; stderr %s" % (stdout, stderr))
    child_env = dict(os.environ)
    child_env.update(set_vars)
    child_env['FSLSUB_JOBID_VAR'] = 'SHELL_JOB_ID'
    child_env['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
    if array_task:
        logger.debug("Adding task variables")
        child_env['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
        child_env['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
        child_env['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
        child_env['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
        child_env['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
        child_env['FSLSUB_PARALLEL'] = '1'
        child_env['SHELL_NCPUS'] = '1'
    else:
        available_cores = _get_cores()
        logger.debug("Found %s cores" % available_cores)
        child_env['SHELL_NCPUS'] = str(available_cores)
        try:
            logger.debug("Removing array task id variable name")
            del child_env['FSLSUB_ARRAYTASKID_VAR']
        except KeyError:
            pass

    if coprocessor is not None and coprocessor_toolkit is not None:
        try:
            load_module(coprocessor, coprocessor_toolkit)
        except UnrecognisedModule:
            raise BadSubmission("Unable to load module " + '/'.join((
                coprocessor, coprocessor_toolkit)))
    jobs = []
    array_args = {}
    job_log = []
    job_log.append(
        "# Built by fsl_sub v.{0} and fsl_sub_plugin_shell v.{1}".format(
            VERSION, plugin_version()
        ))
    job_log.append("# Modules loaded: ")
    job_log.append("\n".join(loaded_modules()))
    job_log.append("# Command line: " + " ".join(sys.argv))
    job_log.append(
        "# Submission time (H:M:S DD/MM/YYYY): " + datetime.datetime.
        now().strftime("%H:%M:%S %d/%m/%Y"))
    job_log.append('')

    to_file = _to_file()

    if array_task:
        logger.debug("Array task requested")
        if not mconf['run_parallel']:
            array_args['parallel_limit'] = 1
        if array_limit is not None:
            logger.debug(
                "Limiting number of parallel tasks to %s" % array_limit)
            array_args['parallel_limit'] = array_limit
        if array_specifier:
            logger.debug(
                "Attempting to parse array specifier %s" % array_specifier)
            (
                array_start,
                array_end,
                array_stride
            ) = parse_array_specifier(array_specifier)
            if not array_start:
                raise BadSubmission("array_specifier doesn't make sense")
            if array_end is None:
                # array_start is the number of jobs
                njobs = array_start
            else:
                njobs = array_end - array_start

                if array_stride is not None:
                    njobs = (njobs // array_stride) + 1
                    array_args['array_stride'] = array_stride
                array_args['array_start'] = array_start
                array_args['array_end'] = array_end
            jobs += njobs * [command]
            job_log.extend(njobs * [' '.join(command)])
            if _disable_parallel(command[0]):
                array_args['parallel_limit'] = 1
            else:
                if array_limit is not None:
                    array_args['parallel_limit'] = array_limit
        else:
            try:
                with open(command[0], 'r') as ll_tasks:
                    command_lines = ll_tasks.readlines()
                for cline in command_lines:
                    if ';' not in cline:
                        jobs.append(shlex.split(cline))
                    else:
                        jobs.append(
                            [bash_cmd(), '-c', cline.strip()])
                    job_log.append(cline)
            except Exception as e:
                raise BadSubmission(
                    "Unable to read array task file "
                    + ' '.join(command)) from e
            if any([_disable_parallel(m[0]) for m in jobs]):
                array_args['parallel_limit'] = 1
            else:
                if array_limit is not None:
                    array_args['parallel_limit'] = array_limit

        if keep_jobscript:
            _write_joblog(job_log, jid, logdir)
        _run_parallel(
            jobs, jid, child_env, to_file, stdout, stderr, **array_args)
    else:
        job_log.append(' '.join(command))
        if keep_jobscript:
            _write_joblog(job_log, jid, logdir)
        control_threads(
            read_config()['thread_control'], available_cores, child_env)
        _run_job(command, jid, child_env, to_file, stdout, stderr)

    return jid


def _write_joblog(job_log, jid, logdir):
    logger = _get_logger()
    log_name = os.path.join(
        logdir,
        '_'.join(('wrapper', str(jid))) + '.sh'
    )
    logger.debug(
        "Requested preservation of job script - storing as " + log_name)
    try:
        with open(log_name, mode='w') as lf:
            writelines_nl(lf, job_log)
    except OSError as e:
        warnings.warn("Unable to preserve wrapper script:" + str(e))


def _run_job(
        job, job_id, child_env,
        to_file=False, stdout_file=None, stderr_file=None):
    logger = _get_logger()
    child_env['SHELL_JOB_ID'] = str(job_id)
    logger.info(
        "executing: " + str(' '.join(job)))
    if to_file:
        try:
            with open(stdout_file, mode='w') as stdout:
                with open(stderr_file, mode='w') as stderr:
                    output = sp.run(
                        job,
                        stdout=stdout,
                        stderr=stderr,
                        universal_newlines=True,
                        env=child_env)
        except (PermissionError, IOError, ) as e:
            return (f"Error in task {job}, "
                    f"unable to open output or error file: {str(e)}")
        except KeyboardInterrupt:
            raise RuntimeError(f"Subtask {job} terminated")
    else:
        try:
            output = sp.run(
                job,
                env=child_env)
        except KeyboardInterrupt:
            raise RuntimeError(f"Subtask {job} terminated")
    if output.returncode != 0:
        if to_file:
            with open(stderr_file, mode='r') as stderr:
                err_msg = stderr.read()
                raise ShellBadSubmission(err_msg, rc=output.returncode)
        else:
            raise ShellBadSubmission("Shell command failed", output.returncode)


def _end_job_number(njobs, start, stride):
    return (njobs - 1) * stride + start


def _mp_run(args):
    job, parent_id, task_id, env, to_file, stdout_file, stderr_file = args
    if not isinstance(task_id, str):
        task_id = str(task_id)
    if not isinstance(parent_id, str):
        parent_id = str(parent_id)
    env['SHELL_JOB_ID'] = parent_id
    env['SHELL_TASK_ID'] = task_id
    log = "Task {0} executed {1}".format(
        task_id,
        ' '.join(job))

    if to_file:
        try:
            with open(stdout_file, mode='w') as stdout:
                with open(stderr_file, mode='w') as stderr:
                    output = sp.run(
                        job,
                        stdout=stdout,
                        stderr=stderr,
                        universal_newlines=True,
                        env=env)
        except (PermissionError, IOError, ) as e:
            return (
                f"Error in subtask {task_id}, unable to open output file: "
                + str(e))
        except KeyboardInterrupt:
            raise RuntimeError("Subtask {0} terminated".format(task_id))
    else:
        try:
            output = sp.run(
                job,
                env=env)
        except KeyboardInterrupt:
            raise RuntimeError("Subtask {0} terminated".format(task_id))
    if output.returncode != 0:
        if to_file:
            with open(stderr_file, mode='r') as stderr:
                return (1, "Task {0} failed executing: {1} ({2})".format(
                    task_id,
                    ' '.join(job),
                    stderr.read()))
        else:
            return (output.returncode, f"Error in sub-task of {task_id}")
    else:
        return (0, log)


def _run_parallel(
        jobs, parent_id, parent_env,
        to_file=False, stdout_file=None, stderr_file=None,
        parallel_limit=None, array_start=1, array_end=None, array_stride=1):
    '''Run jobs in parallel - pass parallel_limit=1 to run array
    tasks linearly'''
    logger = _get_logger()
    if array_end is None:
        array_end = _end_job_number(len(jobs), array_start, array_stride)
    logger.info("Running jobs in parallel")
    available_cores = _get_cores()
    logger.debug("Found %s cores" % available_cores)
    if parallel_limit is not None and available_cores > parallel_limit:
        available_cores = parallel_limit
        logger.debug("Cores limited to %s" % parallel_limit)
    control_threads(read_config()['thread_control'], 1, parent_env)

    logger.debug(
        "Have {0} cores available for parallelising over".format(
            available_cores))

    job_list = []
    for id, job in enumerate(jobs):
        task_id = id + 1
        child_env = dict(parent_env)
        child_to_file = to_file
        if stdout_file != '/dev/null':
            child_stdout = '.'.join((stdout_file, str(task_id)))
        else:
            child_stdout = stdout_file

        if stderr_file != '/dev/null':
            child_stderr = '.'.join((stderr_file, str(task_id)))
        else:
            child_stderr = stderr_file
        child_env['SHELL_JOB_ID'] = str(parent_id)
        child_env['SHELL_TASK_ID'] = str(task_id)
        child_env['SHELL_TASK_FIRST'] = str(array_start)
        child_env['SHELL_TASK_LAST'] = str(array_end)
        child_env['SHELL_TASK_STEPSIZE'] = str(array_stride)
        child_env['SHELL_ARRAYCOUNT'] = ''
        job_list.append(
            [
                job, parent_id, task_id, child_env,
                child_to_file, child_stdout, child_stderr, ])

    job_errors = []
    with get_context("spawn").Pool(available_cores) as pool:
        logger.debug(str(job_list))
        try:
            for out in pool.imap(_mp_run, job_list):
                if out[0]:
                    job_errors.append(out[1])
                else:
                    logger.info(out[1])
        except RuntimeError as e:
            raise BadSubmission from e
        except KeyboardInterrupt:
            raise BadSubmission("Terminated")

    if job_errors:
        raise BadSubmission(
            "Errors occured when running array task in shell plugin: "
            + "\n".join(job_errors))


def _cores():
    '''Obtain maximum number of cores available to us
    (observing any core masking, where OS supports)'''
    logger = _get_logger()
    try:
        available_cores = len(os.sched_getaffinity(0))
        logger.debug(f"Using os.sched_getaffinity, cores: {available_cores}")
    except AttributeError:
        # macOS doesn't support above so fall back to count of all CPUs
        available_cores = os.cpu_count()
        logger.debug(f"Using os.cpu_count, cores: {available_cores}")
    return available_cores


def _get_cores():
    '''Obtain maximum number of cores available to us
    (observing any core masking, where OS supports)'''
    logger = _get_logger()
    available_cores = _cores()
    try:
        fslsub_parallel = int(os.environ['FSLSUB_PARALLEL'])
        if fslsub_parallel > 0 and available_cores > fslsub_parallel:
            available_cores = fslsub_parallel
        logger.debug(
            "Available cores, fslsub_parallel: %s, %s"
            % (available_cores, fslsub_parallel))
    except (KeyError, ValueError, ):
        pass

    return available_cores


def provides_coproc_config():
    return False


def _default_config_file():
    return str(files('fsl_sub').joinpath('plugins', 'fsl_sub_shell.yml'))


def default_conf():
    '''Returns a string containing the default configuration for this
    cluster plugin.'''

    try:
        with open(_default_config_file()) as d_conf_f:
            d_conf = d_conf_f.read()
    except FileNotFoundError as e:
        raise MissingConfiguration(
            "Unable to find default configuration file: " + str(e))
    return d_conf


def job_status(job_id, sub_job_id=None):

    return None
