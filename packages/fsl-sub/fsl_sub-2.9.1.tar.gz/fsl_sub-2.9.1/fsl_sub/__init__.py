#!/usr/bin/env fslpython

# fsl_sub python module

#    Author Duncan Mortimer

import datetime
import getpass
import logging
from operator import itemgetter
import os
import socket
import shlex
import warnings
from math import ceil
from fsl_sub.exceptions import (
    BadConfiguration,
    BadSubmission,
)
from fsl_sub.coprocessors import (
    configure_coprocessor,
)
from fsl_sub.config import (
    get_option,
    read_config,
    method_config,
    uses_projects,
)
import fsl_sub.consts
from fsl_sub.parallel import (
    has_parallel_envs,
)
from fsl_sub.projects import (
    get_project_env,
    project_exists,
)
from fsl_sub.utils import (
    load_plugins,
    build_job_name,
    command_exists,
    get_plugin_qdel,
    control_threads,
    make_logdir,
    human_to_ram,
    update_envvar_list,
    smt_threads,
)
from fsl_sub.version import VERSION


def fsl_sub_warnings_formatter(
        message, category, filename, lineno, file=None, line=None):
    return str(message) + '\n'


warnings.formatwarning = fsl_sub_warnings_formatter
warnings.simplefilter('always', UserWarning)


def version():
    return VERSION


def report(
    job_id,
    subjob_id=None
):
    '''Request a job status. Returns a dictionary:
        id
        name
        script (if available)
        arguments (if available)
        submission_time
        tasks (dict keyed on sub-task ID):
            status:
                fsl_sub.consts.QUEUED
                fsl_sub.consts.RUNNING
                fsl_sub.consts.FINISHED
                fsl_sub.consts.FAILEDNQUEUED
                fsl_sub.consts.SUSPENDED
                fsl_sub.consts.HELD
            start_time
            end_time
            sub_time
            utime
            stime
            exit_status
            error_message
            maxmemory (in Mbytes)
        parents (if available)
        children (if available)
        job_directory (if available)
    '''

    PLUGINS = load_plugins()

    config = read_config()

    if config['method'] == 'shell':
        ntime = datetime.datetime.now()
        return {
            'id': 123456,
            'name': 'nojob',
            'script': None,
            'arguments': None,
            'submission_time': ntime,
            'tasks': {
                '1': {
                    'status': fsl_sub.consts.FINISHED,
                    'start_time': ntime,
                    'end_time': ntime,
                    'sub_time': ntime,
                    'utime': 0,
                    'stime': 0,
                    'exit_status': 0,
                    'error_message': None,
                    'maxmemory': 0
                }
            },
            'parents': None,
            'children': None,
            'job_directory': None,
            'fake': True
        }
    grid_module = 'fsl_sub_plugin_' + config['method']
    if grid_module not in PLUGINS:
        raise BadConfiguration(
            "{} not a supported method".format(config['method']))

    try:
        job_status = PLUGINS[grid_module].job_status
    except AttributeError as e:
        raise BadConfiguration(
            "Failed to load plugin " + grid_module
            + " ({0})".format(str(e))
        )

    return job_status(job_id, subjob_id)


def submit(
    command,
    name=None,
    threads=1,
    queue=None,
    jobhold=None,
    array_task=False,
    array_hold=None,
    array_limit=None,
    array_specifier=None,
    parallel_env=None,
    jobram=None,
    jobtime=None,
    resources=None,
    ramsplit=True,
    priority=None,
    validate_command=True,
    mail_on=None,
    mailto="{username}@{hostname}".format(
        username=getpass.getuser(),
        hostname=socket.gethostname()),
    logdir=None,
    coprocessor=None,
    coprocessor_toolkit=None,
    coprocessor_class=None,
    coprocessor_class_strict=False,
    coprocessor_multi="1",
    usescript=False,
    architecture=None,
    requeueable=True,
    as_tuple=False,
    project=None,
    export_vars=None,
    keep_jobscript=False,
    extra_args=None,
):
    '''Submit job(s) to a queue, returns the job id as an int (
    pass as_tuple=True to return a single value tuple).
    Single tasks require a command in the form of a list [command, arg1,
    arg2, ...] or simple string "command arg1 arg2".
    Array tasks (array_task=True) require a file name of the array task table
    file unless array_specifier(=n[-m[:s]]) is specified in which case command
    is as per a single task.

    Requires:

    command - string or list containing command to run
                or the file name of the array task file.
                If array_specifier is given then this must be
                a string/list containing the command to run.

    Optional:
    name - Symbolic name for task (defaults to first component of command)
    array_task - is the command is an array task (defaults to False)
    jobhold - id(s) of jobs to hold for (string or list)
    array_hold - complex hold string, integer or list
    array_limit - limit concurrently scheduled array
            tasks to specified number
    array_specifier - n[-m[:s]] n subtasks or starts at n, ends at m with
            a step of s.
    as_tuple - if true then return job ID as a single value tuple
    parallel_env - parallel environment name
    jobram - RAM required by job (total of all threads)
    jobtime - time (in minutes for task)
    requeueable - job may be requeued on node failure
    resources - list of resource request strings
    ramsplit - break tasks into multiple slots to meet RAM constraints
    priority - job priority (0-1023)
    mail_on - mail user on 'a'bort or reschedule, 'b'egin, 'e'nd,
            's'uspended, 'n'o mail
    mailto - email address to receive job info
    logdir - directory to put log files in
    coprocessor - name of coprocessor required
    coprocessor_toolkit - coprocessor toolkit version
    coprocessor_class - class of coprocessor required
    coprocessor_class_strict - whether to choose only this class
            or all more capable
    coprocessor_multi - how many coprocessors you need (or
            complex description) (int or string)
    queue - Explicit queue to submit to - use jobram/jobtime in preference to
            this
    usescript - queue config is defined in script
    project - Cluster project to submit job to, defaults to None
    export_vars - list of environment variables to preserve for job
            ignored if job is copying complete environment
    keep_jobscript - whether to generate and keep a script defining the
            parameters used to run your task
    validate_command - whether to validate the command or not.
    extra_args - list of additional argument strings to pass to the cluster
            scheduler.
    '''
    logger = logging.getLogger(__name__)
    try:
        debugging = os.environ['FSLSUB_DEBUG'] == '1'
    except KeyError:
        debugging = False
    if debugging:
        update_envvar_list(export_vars, 'FSLSUB_DEBUG=1')
        logger.setLevel(logging.DEBUG)

    # Can't just have export_vars=[] in function definition as the list is
    # mutable so subsequent calls will return the updated list!
    if export_vars is None:
        export_vars = []
    my_export_vars = list(export_vars)

    # Ensure FSLSUB's configuration file path is propagated to jobs
    if 'FSLSUB_CONF' in os.environ.keys():
        update_envvar_list(
            my_export_vars,
            '='.join(('FSLSUB_CONF', os.environ['FSLSUB_CONF'])))

    logger.debug("Submit called with:")
    logger.debug(
        " ".join(
            [
                str(a) for a in [
                    command, name, threads, queue, jobhold, array_task,
                    array_hold, array_limit, array_specifier, parallel_env,
                    jobram, jobtime, resources, ramsplit, priority,
                    validate_command, mail_on, mailto, logdir,
                    coprocessor, coprocessor_toolkit, coprocessor_class,
                    coprocessor_class_strict, coprocessor_multi,
                    usescript, architecture, requeueable,
                    as_tuple, project, extra_args,
                ]
            ]
        )
    )

    PLUGINS = load_plugins()

    config = read_config()
    fsl_sub.config.validate_config(config)
    grid_module = 'fsl_sub_plugin_' + config['method']
    if grid_module not in PLUGINS:
        raise BadConfiguration(
            "{} not a supported method".format(config['method']))

    try:
        already_queued = PLUGINS[grid_module].already_queued
        qtest = PLUGINS[grid_module].qtest
    except AttributeError as e:
        raise BadConfiguration(
            "Failed to load plugin " + grid_module
            + " ({0})".format(str(e))
        )

    if config['method'] != 'shell':
        if already_queued():
            config['method'] = 'shell'
            warnings.warn(
                'Warning: job on queue attempted to submit more jobs -'
                'running jobs using shell plugin instead.'
            )

    config['qtest'] = qtest()
    if config['qtest'] is None:
        config['method'] = 'shell'
        warnings.warn(
            'Warning: fsl_sub configured for {0} but {0}'
            ' software not found.'.format(config['method'])
        )

    logger.debug("Configuring plugin " + config['method'])
    # Reset grid_module in case we've switched to the Shell plugin
    grid_module = 'fsl_sub_plugin_' + config['method']
    try:
        queue_submit = PLUGINS[grid_module].submit
        qtest = PLUGINS[grid_module].qtest
        queue_exists = PLUGINS[grid_module].queue_exists
        BadSubmission = PLUGINS[grid_module].BadSubmission
        already_queued = PLUGINS[grid_module].already_queued
    except AttributeError as e:
        raise BadConfiguration(
            "Failed to load plugin " + grid_module
            + " ({0})".format(str(e))
        )

    if isinstance(command, str) or len(command) == 1:
        # command is a basic string or single element list
        logger.debug("Simple string or single element list passed")
        if isinstance(command, list):
            command = command[0]
        if ';' not in command:
            logger.debug("String being shlex split")
            command = shlex.split(command)
        else:
            # Command is a shell one-liner, we can't reliably split this
            logger.debug("String contains ';' we cannot split it")
            command = [command]
            logger.debug("Disabling validation")
            validate_command = False
        logger.debug(command)
    elif not isinstance(command, list):
        raise BadSubmission("Command should be a list or string")

    logger.debug("Loading configuration for " + config['method'])
    mconfig = method_config(config['method'])
    logger.debug("Method configuration is " + str(mconfig))

    logger.debug(
        "Adding export_vars from config to provided list "
        + str(my_export_vars) + str(config.get('export_vars', [])))
    [update_envvar_list(
        my_export_vars, a, overwrite=False) for a in config.get(
            'export_vars', [],)]

    if has_parallel_envs():
        parallel_env_requested = parallel_env
    else:
        parallel_env_requested = None

    make_logdir(logdir)

    if jobram is None:
        try:
            mem_requested = human_to_ram(
                os.environ['FSLSUB_MEMORY_REQUIRED'],
                fsl_sub.consts.RAMUNITS,
                as_int=True)
        except KeyError:
            pass
        except ValueError:
            warnings.warn("FSLSUB_MEMORY_REQUIRED variable doesn't make sense")
        else:
            jobram = mem_requested

    if mconfig['mail_support'] is True:
        if mail_on is None:
            try:
                mail_on = mconfig['mail_mode']
            except KeyError:
                warnings.warn(
                    "Mail not configured but enabled in configuration for "
                    + config['method'])
        else:
            # Mail modes is a dictionary
            if mail_on not in mconfig['mail_modes']:
                raise BadSubmission(
                    "Unrecognised mail mode " + mail_on)

    # For simple numbers pass these in as list, if they are strings
    # then leave them alone
    if jobhold is not None:
        if not isinstance(jobhold, (str, int, list, tuple)):
            raise BadSubmission(
                "jobhold must be a string, int, list or tuple")
    if array_hold is not None:
        if not isinstance(array_hold, (str, int, list, tuple)):
            raise BadSubmission(
                "array_hold must be a string, int, list or tuple")

    validate_type = 'command'
    if array_task is False:
        job_type = 'single'
        if (
                array_hold is not None
                or array_limit is not None
                or array_specifier is not None):
            raise BadSubmission(
                "Array controls not applicable to non-array tasks")
    elif array_specifier is None:
        job_type = 'array file'
        validate_type = 'array'
    else:
        job_type = 'array aware command'
        validate_type = 'command'

    logger.info(
        "METHOD={0} : TYPE={1} : args={2}".format(
            config['method'],
            job_type,
            " ".join(command)
        ))

    if validate_command:
        command_exists(
            command[0], ctype=validate_type,
            usescript=usescript)

    override_queue = get_option(
        'OVERRIDE_QUEUE', options={},
        default=False
    )

    if name is None:
        task_name = build_job_name(command)
        logger.debug("No name passed - setting to " + task_name)
    else:
        task_name = name

    if mconfig['queues'] is False:
        queue = None
        split_on_ram = None
        queue_conf = {}
    else:
        if not override_queue:
            split_on_ram = mconfig.get('map_ram', True) and ramsplit
        else:
            split_on_ram = False
        if (split_on_ram
                and parallel_env is None
                and 'large_job_split_pe' in mconfig):
            parallel_env = mconfig['large_job_split_pe']
        else:
            parallel_env = parallel_env_requested

        if override_queue:
            if override_queue not in config['queues']:
                # Must specify a queue/partition name
                logger.debug(
                    f"FSLSUB_OVERRIDE_QUEUE ({override_queue}) "
                    "not a valid queue name")
                warnings.warn(
                    "FSLSUB_OVERRIDE_QUEUE set to the name of an "
                    "unknown partition/queue")

            queue = override_queue

        if queue is None:
            queue_details = getq_and_slots(
                job_time=jobtime,
                job_ram=jobram,
                job_threads=threads,
                queues=config['queues'],
                coprocessor=coprocessor,
                coprocessor_multi=coprocessor_multi,
                ll_env=parallel_env
            )
            logger.debug("Automatic queue selection:")
            (queue, slots_required) = queue_details
            logger.debug(queue_details)
        else:
            if not queue_exists(queue):
                raise BadSubmission("Unrecognised queue " + queue)
            logger.debug("Specific queue: " + queue)
            if override_queue:
                slots_required = threads
            else:
                slots_required = _slots_required(
                    queue, jobram, config['queues'], threads)

        threads = max(slots_required, threads)

        if threads == 1 and parallel_env_requested is None:
            parallel_env = None
        if threads > 1 and parallel_env is None and has_parallel_envs(config):
            raise BadSubmission(
                "Job requires {} slots but no parallel environment "
                "available or requested".format(threads))
        if threads > 1 and mconfig.get('thread_ram_divide', False) and not split_on_ram:  # noqa E501
            split_on_ram = True

        try:
            queue_conf = config['queues'][queue]
        except KeyError:
            queue_conf = {}

    (gpu_threads, parallel_env) = configure_coprocessor(
        queue, threads, parallel_env,
        coprocessor, coprocessor_multi,
        coprocessor_toolkit)

    if not override_queue:
        threads = gpu_threads

    threads = smt_threads(threads, queue_conf)

    control_threads(
        config['thread_control'], threads,
        add_to_list=my_export_vars)

    if uses_projects():
        q_project = get_project_env(project)
        if q_project is not None and not project_exists(q_project):
            raise BadSubmission(
                "Project not recognised"
            )
    else:
        q_project = None

    extra_args = _process_extra_args(extra_args)

    logger.debug(
        "Calling queue_submit fsl_sub_plugin_{0} with: ".format(
            config['method']))
    logger.debug(
        ", ".join(
            [str(a) for a in [
                command, task_name, queue, jobhold, array_task,
                array_hold, array_limit, array_specifier, parallel_env,
                jobram, jobtime, resources, ramsplit, priority,
                mail_on, mailto, logdir, coprocessor, coprocessor_toolkit,
                coprocessor_class, coprocessor_class_strict, coprocessor_multi,
                usescript, architecture, requeueable, extra_args]]))

    job_id = queue_submit(
        command,
        job_name=task_name,
        threads=threads,
        queue=queue,
        jobhold=jobhold,
        array_task=array_task,
        array_hold=array_hold,
        array_limit=array_limit,
        array_specifier=array_specifier,
        parallel_env=parallel_env,
        jobram=jobram,
        jobtime=jobtime,
        resources=resources,
        ramsplit=split_on_ram,
        priority=priority,
        mail_on=mail_on,
        mailto=mailto,
        logdir=logdir,
        coprocessor=coprocessor,
        coprocessor_toolkit=coprocessor_toolkit,
        coprocessor_class=coprocessor_class,
        coprocessor_class_strict=coprocessor_class_strict,
        coprocessor_multi=coprocessor_multi,
        usescript=usescript,
        architecture=architecture,
        requeueable=requeueable,
        project=q_project,
        export_vars=my_export_vars,
        keep_jobscript=keep_jobscript,
        extra_args=extra_args
    )

    if as_tuple:
        return (job_id,)
    else:
        return job_id


def _process_extra_args(extra_args, env=os.environ):
    '''Look for FSLSUB_EXTRA_* environment variables and merge their values
    with the list of additional arguments passed in 'extra_args'.'''
    # Process extra argument environment variables
    extra_env_vars = [
        v for k, v in env.items() if k.startswith('FSLSUB_EXTRA_')]
    # Command line overrides environment variables
    if extra_args is not None:
        arg_dict = {k.split('=', 1)[0]: (k.split('=', 1)[1] if '=' in k else '') for k in extra_args}  # noqa E501
    else:
        arg_dict = {}
    if extra_env_vars:
        extra_env_vars_dict = {k.split('=', 1)[0]: (k.split('=', 1)[1] if '=' in k else '') for k in extra_env_vars}  # noqa E501
    else:
        extra_env_vars_dict = {}
    extra_env_vars_dict.update(arg_dict)

    extra_args = [
        '='.join((k, v)) if v else k for k, v in extra_env_vars_dict.items()]
    if not extra_args:
        return None
    return extra_args


def _slots_required(q_name, jobram, qconfig, threads):
    logger = logging.getLogger(__name__)
    if '@' in q_name:
        logger.debug("q@host requested, removing @host from all queues")
        q_name = ','.join([q.split('@')[0] for q in q_name.split(',')])
    if q_name in qconfig:
        return calc_slots(
            jobram,
            qconfig[q_name]['slot_size'],
            threads)
    else:
        logger.debug("queue definition not found, defaulting to single slot")
        return 1


def calc_slots(job_ram, slot_size, job_threads):
    '''Calculate how many slots would be necessary to
    provide this job request'''
    logger = logging.getLogger(__name__)
    logger.debug(
        "Calc slots based on JR:SS:JT - {0}:{1}:{2}".format(
            job_ram, slot_size, job_threads
        ))
    if job_ram == 0 or job_ram is None:
        return max(1, job_threads)
    else:
        if slot_size is not None:
            return max(int(ceil(job_ram / slot_size)), job_threads)
        return job_threads


def getq_and_slots(
        queues, job_time=0, job_ram=0,
        job_threads=1, coprocessor=None, coprocessor_multi=1,
        ll_env=None):
    '''Calculate which queue to run the job on. job_time is in minutes,
    job_ram in units given in configuration.
    Still needs job splitting across slots'''
    logger = logging.getLogger(__name__)
    if job_ram is None:
        job_ram = 0

    queue_list = list(queues.keys())

    if not queue_list:
        raise BadSubmission("No queues found")

    # Filter on coprocessor availability
    if coprocessor is not None:
        try:
            num_cprocs = int(coprocessor_multi)
        except ValueError:
            num_cprocs = 1

        queue_list = [
            q for q in queue_list if 'copros' in queues[q]
            and coprocessor in queues[q]['copros']]
        if not queue_list:
            raise BadSubmission("No queues with requested co-processor found")
    else:
        tq = []
        for q in queue_list:
            qd = queues[q]
            if 'copros' not in qd:
                tq.append(q)
            else:
                qdcp = qd['copros']
                if not all([qdcp[c].get('exclusive', True) for c in qdcp]):
                    tq.append(q)
        queue_list = tq
        if not queue_list:
            raise BadSubmission(
                "No queues found without co-processors defined that "
                "are non-exclusive")

    # Filter on parallel environment availability
    if ll_env is not None:
        queue_list = [
            q for q in queue_list if 'parallel_envs' in queues[q]
            and ll_env in queues[q]['parallel_envs']
        ]
        if not queue_list:
            raise BadSubmission(
                "No queues with requested parallel environment found")

    # If no job time was specified then find the default queues
    # (if defined)
    if job_time is None or job_time == 0:
        d_queues = [
            q for q in queue_list if 'default' in queues[q]
        ]
        if d_queues:
            queue_list = d_queues

        job_time = 0

    slots = {}
    for index, q in enumerate(queue_list):
        if coprocessor is None:
            slots[q] = calc_slots(
                job_ram, queues[q]['slot_size'], job_threads)
        else:
            slots[q] = min(num_cprocs, queues[q]['max_slots'])
        # If group/priority not specified then create pseudo-groups,
        # one for each queue
        if 'group' not in queues[q].keys():
            queues[q]['group'] = index
        if 'priority' not in queues[q].keys():
            queues[q]['priority'] = 1

    # Produce list of tuples with (queue, group, priority, max time,
    # slots required by job)
    queue_def_list = [
        (
            q, queues[q]['group'], queues[q]['priority'],
            queues[q]['time'], slots[q]) for q in queue_list]

    # Sort reverse priority
    queue_def_list.sort(key=itemgetter(2), reverse=True)
    # Sort on group
    queue_def_list.sort(key=itemgetter(1))
    # Sort on time
    queue_def_list.sort(key=itemgetter(3))
    # Sort on slots required
    queue_def_list.sort(key=itemgetter(4))

    queue_list = [q[0] for q in queue_def_list]
    ql = [
        q for q in queue_list if queues[q]['time'] >= job_time
        and queues[q]['max_size'] >= job_ram
        and queues[q]['max_slots'] >= job_threads]
    if not ql:
        raise BadSubmission(
            "No queues matching time/RAM/thread requirements found")

    logger.info(
        "Estimated RAM was {0} GBm, runtime was {1} minutes.\n".format(
            job_ram, job_time
        ))
    if coprocessor:
        logger.info("Co-processor {} was requested".format(coprocessor))
    if len(ql):
        logger.info(
            "Appropriate queue is {}".format(ql[0]))
    try:
        q_tuple = (ql[0], slots[ql[0]], )
    except IndexError:
        raise BadSubmission("No matching queues found")
    return q_tuple


def delete_job(job_id):
    '''Function that attemps to kill a job (either cluster or shell)'''
    PLUGINS = load_plugins()

    config = read_config()

    grid_module = 'fsl_sub_plugin_' + config['method']
    if grid_module not in PLUGINS:
        raise BadConfiguration(
            "{} not a supported method".format(config['method']))

    try:
        already_queued = PLUGINS[grid_module].already_queued
    except AttributeError as e:
        raise BadConfiguration(
            "Failed to load plugin " + grid_module
            + " ({0})".format(str(e))
        )
    if already_queued():
        config['method'] = 'shell'
    return get_plugin_qdel(config['method'])(job_id)
