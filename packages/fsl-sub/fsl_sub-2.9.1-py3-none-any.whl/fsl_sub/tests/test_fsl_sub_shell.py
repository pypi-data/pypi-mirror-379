#!/usr/bin/env python
import os
import tempfile
import shlex
import subprocess
import unittest
import fsl_sub.plugins.fsl_sub_plugin_shell
import fsl_sub.exceptions
from unittest.mock import (patch, ANY)
from fsl_sub.utils import bash_cmd


class TestRequireMethods(unittest.TestCase):
    def test_available_methods(self):
        methods = dir(fsl_sub.plugins.fsl_sub_plugin_shell)
        for method in [
                'plugin_version', 'qtest', 'queue_exists',
                'submit', 'default_conf', 'job_status']:
            with self.subTest(method):
                self.assertTrue(method in methods)


class TestUtils(unittest.TestCase):
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._cores', autospec=True)
    def test__get_cores(self, mock__cores):
        mock__cores.return_value = 4
        with patch.dict(
                'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ', clear=True):
            with self.subTest("No envvar"):
                self.assertEqual(
                    fsl_sub.plugins.fsl_sub_plugin_shell._get_cores(),
                    4
                )

        with self.subTest("With envvar"):
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    {'FSLSUB_PARALLEL': "2", }):
                self.assertEqual(
                    fsl_sub.plugins.fsl_sub_plugin_shell._get_cores(),
                    2
                )

        with self.subTest("With envvar=0"):
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    {'FSLSUB_PARALLEL': "0", }):
                self.assertEqual(
                    fsl_sub.plugins.fsl_sub_plugin_shell._get_cores(),
                    4
                )

    def test__run_job(self):
        with self.subTest('To files'):
            with tempfile.NamedTemporaryFile(mode='w') as stdout_f:
                with tempfile.NamedTemporaryFile(mode='w') as stderr_f:
                    fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
                        ['echo', 'a string'], 1234, {}, True,
                        stdout_f.name, stderr_f.name)

                    with open(stdout_f.name, 'r') as sout:
                        with open(stderr_f.name, 'r') as serr:
                            output = sout.read()
                            errors = serr.read()
            self.assertEqual(output.strip(), 'a string')
            self.assertEqual(errors.strip(), '')

            with self.subTest("To files with error"):
                with tempfile.TemporaryDirectory() as tempdir:
                    err_script = os.path.join(tempdir, 'err_script')
                    with open(err_script, 'wt') as f:
                        f.write("#!/bin/sh\necho Failed >&2\nexit 1\n")

                    os.chmod(err_script, 0o755)

                    with tempfile.NamedTemporaryFile(mode='w') as stdout_f:
                        with tempfile.NamedTemporaryFile(mode='w') as stderr_f:
                            with self.assertRaises(fsl_sub.exceptions.ShellBadSubmission) as ex:  # noqa E501
                                fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
                                    [err_script], 1234, {},
                                    True, stdout_f.name, stderr_f.name)
                            rc = ex.exception.rc
                            self.assertEqual(str(ex.exception), "Failed\n")
                            self.assertEqual(rc, 1)

            with patch('fsl_sub.plugins.fsl_sub_plugin_shell.sp.run') as mock_spr:  # noqa E501
                job = ['echo', 'a string']
                mock_spr.return_value = subprocess.CompletedProcess(
                    job,
                    returncode=0
                )
                with self.subTest("To stdout"):
                    fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
                        job, 1234, {}, False, '', '')
                    mock_spr.assert_called_with(
                        job,
                        env={'JOB_ID': '1234',
                             'SHELL_NCPUS': '1'})
                mock_spr.reset_mock()
                mock_spr.return_value = subprocess.CompletedProcess(
                    job,
                    stderr="Failed",
                    returncode=1
                )
                with self.subTest("To stdout with error"):
                    with self.assertRaises(fsl_sub.exceptions.ShellBadSubmission) as ex:  # noqa E501
                        fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
                            ['sh', '-c', '"exit 1"'], 1234, {}, False, '', '')
                    rc = ex.exception.rc
                    self.assertEqual(rc, 1)
                    self.assertEqual(str(ex.exception), 'Shell command failed')

    def test__end_job_number(self):
        self.assertEqual(
            9, fsl_sub.plugins.fsl_sub_plugin_shell._end_job_number(5, 1, 2))
        self.assertEqual(
            10, fsl_sub.plugins.fsl_sub_plugin_shell._end_job_number(4, 1, 3))
        self.assertEqual(
            10, fsl_sub.plugins.fsl_sub_plugin_shell._end_job_number(3, 4, 3))

    def test__disable_parallel(self):
        with patch(
                'fsl_sub.plugins.fsl_sub_plugin_shell.method_config',
                autospec=True) as mock_mc:
            with self.subTest("Is"):
                mock_mc.return_value = {
                    'parallel_disable_matches': ['mycommand', ]}
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand2'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('amycommand'))  # noqa E501
            with self.subTest("Is (absolute)"):
                mock_mc.return_value = {
                    'parallel_disable_matches': ['/usr/local/bin/mycommand', ]}
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand2'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('amycommand'))  # noqa E501
            with self.subTest("Absolute wildcards - start"):
                mock_mc.return_value = {
                    'parallel_disable_matches': [
                        '/usr/local/bin/*_mycommand', ]}
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/bad_mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand2'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('amycommand'))  # noqa E501
            with self.subTest("Absolute wildcards - end"):
                mock_mc.return_value = {
                    'parallel_disable_matches': [
                        '/usr/local/bin/mycommand_*', ]}
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/mycommand_bad'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand2'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('amycommand'))  # noqa E501
            with self.subTest("Starts"):
                mock_mc.return_value = {
                    'parallel_disable_matches': ['mycommand_*', ]}
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand_'))  # noqa E501
                self.assertTrue(
                    fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/mycommand_special'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand_special'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand_special'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('amycommand_special'))  # noqa E501
            with self.subTest("Ends"):
                mock_mc.return_value = {
                    'parallel_disable_matches': ['*_special', ]}
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('_special'))  # noqa E501
                self.assertTrue(
                    fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('/usr/local/bin/mycommand_special'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand_special'))  # noqa E501
                self.assertTrue(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('./mycommand_special'))  # noqa E501
                self.assertFalse(fsl_sub.plugins.fsl_sub_plugin_shell._disable_parallel('mycommand_specialb'))  # noqa E501


class TestShell(unittest.TestCase):
    def setUp(self):
        self.outdir = tempfile.TemporaryDirectory()
        self.patch_objects = {
            'fsl_sub.plugins.fsl_sub_plugin_shell._to_file': {
                'autospec': True, 'return_value': False, },
        }
        self.patches = {}
        for p, kwargs in self.patch_objects.items():
            self.patches[p] = patch(p, **kwargs)
        self.mocks = {}
        for o, p in self.patches.items():
            self.mocks[o] = p.start()

        self.addCleanup(patch.stopall)

    def tearDown(self):
        self.outdir.cleanup()

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.sp.run', autospec=True)
    def test_simple_job(self, mock_spr):
        job = ["echo", "Hello"]
        mock_spr.return_value = subprocess.CompletedProcess(
            job, returncode=0
        )

        with patch.dict(
                'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ', {},
                clear=True):
            jid = fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                job,
                job_name='echo',
                logdir=self.outdir.name
            )

        mock_spr.assert_called_with(
            job,
            env={
                'FSLSUB_JOBID_VAR': 'JOB_ID',
                'FSLSUB_NSLOTS': 'SHELL_NCPUS',
                'JOB_ID': f"{jid}",
                'SHELL_NCPUS': '1'}
        )

    def test_complex_job(self):
        with self.subTest("Two commands"):
            job = ["sleep 0.1; touch " + os.path.join(
                self.outdir.name, 'testfile')]
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                job,
                job_name='echo',
                logdir=self.outdir.name
            )

            self.assertTrue(
                os.path.exists(
                    os.path.join(self.outdir.name, 'testfile')))

        with self.subTest("Three commands"):
            job = [
                "sleep 0.1; touch " + os.path.join(
                    self.outdir.name, 'testfile1')
                + '; touch ' + os.path.join(
                    self.outdir.name, 'testfile2')]
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                job,
                job_name='echo',
                logdir=self.outdir.name
            )

            self.assertTrue(
                os.path.exists(
                    os.path.join(self.outdir.name, 'testfile1')))
            self.assertTrue(
                os.path.exists(
                    os.path.join(self.outdir.name, 'testfile2')))

        with self.subTest("Piped commands 1"):
            testscript = os.path.join(self.outdir.name, 'testscript')
            with open(testscript, 'w') as ts:
                ts.write('''#!/bin/sh
echo "Hello"
''')
            os.chmod(testscript, 0o755)
            job = [
                testscript, ">", os.path.join(
                    self.outdir.name, 'testfile3')]
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                job,
                job_name='echo',
                logdir=self.outdir.name
            )

            self.assertTrue(
                os.path.exists(
                    os.path.join(self.outdir.name, 'testfile3')))
            with open(os.path.join(self.outdir.name, 'testfile3')) as tf:
                self.assertEqual(
                    'Hello\n',
                    tf.read()
                )

        with self.subTest("Piped commands 2"):
            job = [
                "echo", "'Hello'", "|", "tr", "-d", "'H'", ">", os.path.join(
                    self.outdir.name, 'testfile4')]
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                job,
                job_name='echo',
                logdir=self.outdir.name
            )

            self.assertTrue(
                os.path.exists(
                    os.path.join(self.outdir.name, 'testfile4')))
            with open(os.path.join(self.outdir.name, 'testfile4')) as tf:
                self.assertEqual(
                    'ello\n',
                    tf.read()
                )

    def test_set_environment(self):
        self.mocks['fsl_sub.plugins.fsl_sub_plugin_shell._to_file'].return_value = True  # noqa E501
        job = [
            bash_cmd(), '-c', "'echo $FSLSUBTEST_ENVVAR > "
            + os.path.join(
                self.outdir.name, 'envvar') + "'", ]
        fsl_sub.plugins.fsl_sub_plugin_shell.submit(
            job,
            job_name='echo',
            logdir=self.outdir.name,
            export_vars=['FSLSUBTEST_ENVVAR=1234', ]
        )

        self.assertTrue(
            os.path.exists(
                os.path.join(self.outdir.name, 'envvar')))
        with open(os.path.join(self.outdir.name, 'envvar')) as tf:
            self.assertEqual(
                '1234\n',
                tf.read()
            )

    def test_set_complexenvironment(self):
        self.mocks['fsl_sub.plugins.fsl_sub_plugin_shell._to_file'].return_value = True  # noqa E501
        job = [
            bash_cmd(), '-c', "'echo $FSLSUBTEST_ENVVAR > "
            + os.path.join(
                self.outdir.name, 'envvar2') + "'", ]
        fsl_sub.plugins.fsl_sub_plugin_shell.submit(
            job,
            job_name='echo',
            logdir=self.outdir.name,
            export_vars=['FSLSUBTEST_ENVVAR=abcd=5678', ]
        )

        self.assertTrue(
            os.path.exists(
                os.path.join(self.outdir.name, 'envvar2')))
        with open(os.path.join(self.outdir.name, 'envvar2')) as tf:
            self.assertEqual(
                'abcd=5678\n',
                tf.read()
            )


@patch(
    'fsl_sub.plugins.fsl_sub_plugin_shell._to_file', return_value=True)
@patch(
    'fsl_sub.plugins.fsl_sub_plugin_shell.bash_cmd',
    return_value="/bin/bash")
class TestShell__run(unittest.TestCase):
    def setUp(self):
        self.pid = os.getpid()
        self.outdir = tempfile.TemporaryDirectory()
        self.job = os.path.join(self.outdir.name, 'jobfile')
        self.errorjob = os.path.join(self.outdir.name, 'errorfile')
        self.stdout = os.path.join(self.outdir.name, 'stdout')
        self.stderr = os.path.join(self.outdir.name, 'stderr')
        self.job_id = 111
        self.p_env = {}
        self.bash = '/bin/bash'
        self.p_env['FSLSUB_JOBID_VAR'] = 'JOB_ID'
        self.p_env['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
        self.p_env['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
        self.p_env['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
        self.p_env['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
        self.p_env['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
        with open(self.job, mode='w') as jobfile:
            jobfile.write(
                '''#!{0}
echo "jobid:${{!FSLSUB_JOBID_VAR}}"
echo "slots:${{!FSLSUB_NSLOTS}}"
echo "taskid:${{!FSLSUB_ARRAYTASKID_VAR}}"
echo "start:${{!FSLSUB_ARRAYSTARTID_VAR}}"
echo "end:${{!FSLSUB_ARRAYENDID_VAR}}"
echo "step:${{!FSLSUB_ARRAYSTEPSIZE_VAR}}"
'''.format(self.bash)
            )
        with open(self.errorjob, mode='w') as jobfile:
            jobfile.write(
                '''#!{0}
echo "jobid:${{!FSLSUB_JOBID_VAR}}" >&2
echo "slots:${{!FSLSUB_NSLOTS}}" >&2
echo "taskid:${{!FSLSUB_ARRAYTASKID_VAR}}" >&2
echo "start:${{!FSLSUB_ARRAYSTARTID_VAR}}" >&2
echo "end:${{!FSLSUB_ARRAYENDID_VAR}}" >&2
echo "step:${{!FSLSUB_ARRAYSTEPSIZE_VAR}}" >&2
exit 2
'''.format(self.bash)
            )
        os.chmod(self.job, 0o755)
        os.chmod(self.errorjob, 0o755)

    def tearDown(self):
        self.outdir.cleanup()

    def test__run_job(self, *args):
        job = [self.job]
        fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
            job, self.job_id, self.p_env,
            to_file=True, stdout_file=self.stdout, stderr_file=self.stderr
        )

        with open(self.stdout, 'r') as jobout:
            joboutput = jobout.read()

        self.assertEqual(
            joboutput,
            f'''jobid:{self.job_id}
slots:1
taskid:
start:
end:
step:
''')

    def test__run_job_stderr(self, *args):
        job = [self.errorjob]
        errout = f'''jobid:{self.job_id}
slots:1
taskid:
start:
end:
step:
'''
        with self.assertRaises(fsl_sub.exceptions.ShellBadSubmission) as bs:
            fsl_sub.plugins.fsl_sub_plugin_shell._run_job(
                job, self.job_id, self.p_env,
                to_file=True,
                stdout_file=self.stdout, stderr_file=self.stderr)

        emess = str(bs.exception)
        self.assertEqual(emess, errout)
        with open(self.stderr, 'r') as jobout:
            joboutput = jobout.read()
        self.assertEqual(joboutput, errout)

    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell._get_cores',
        autospec=True)
    def test__run_parallel_all(self, mock_gc, *args):
        jobs = [self.job, self.job, self.job, ]

        mock_gc.return_value = 4
        fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel(
            jobs, self.job_id, self.p_env,
            to_file=True, stdout_file=self.stdout, stderr_file=self.stderr
        )
        job_list = []
        for subjob in (1, 2, 3):
            jobout = '.'.join((self.stdout, str(subjob)))
            joberr = '.'.join((self.stderr, str(subjob)))
            child_env = dict(self.p_env)
            child_env['JOB_ID'] = self.job_id
            child_env['SHELL_TASK_ID'] = subjob
            child_env['SHELL_TASK_FIRST'] = 1
            child_env['SHELL_TASK_LAST'] = 3
            child_env['SHELL_TASK_STEPSIZE'] = 1
            with open(jobout, 'r') as jout:
                joboutput = jout.read()
            with open(joberr, 'r') as jerr:
                joberror = jerr.read()
            job_list.append([self.job, subjob, child_env, jobout, joberr])
            self.assertEqual(
                joboutput,
                '''jobid:{0}
slots:{1}
taskid:{2}
start:{3}
end:{4}
step:{5}
'''.format(self.job_id, 1, subjob, 1, 3, 1))
            self.assertEqual(joberror, '')

    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell._get_cores',
        autospec=True)
    def test__run_parallel_cpulimited(self, mock_gc, *args):
        mock_gc.return_value = 2

        jobs = [self.job, self.job, self.job, ]

        fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel(
            jobs, self.job_id, self.p_env,
            to_file=True,
            stdout_file=self.stdout, stderr_file=self.stderr
        )

        job_list = []
        for subjob in (1, 2, 3):
            jobout = '.'.join((self.stdout, str(subjob)))
            joberr = '.'.join((self.stderr, str(subjob)))
            child_env = dict(self.p_env)
            child_env['JOB_ID'] = self.job_id
            child_env['SHELL_TASK_ID'] = str(subjob)
            child_env['SHELL_TASK_FIRST'] = str(1)
            child_env['SHELL_TASK_LAST'] = str(3)
            child_env['SHELL_TASK_STEPSIZE'] = str(1)
            with open(jobout, 'r') as jout:
                joboutput = jout.read()
            with open(joberr, 'r') as jerr:
                joberror = jerr.read()
            job_list.append([self.job, subjob, child_env, jobout, joberr])
            self.assertEqual(
                joboutput,
                '''jobid:{0}
slots:{1}
taskid:{2}
start:{3}
end:{4}
step:{5}
'''.format(self.job_id, 1, subjob, 1, 3, 1))
            self.assertEqual(joberror, '')

    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell._get_cores',
        autospec=True)
    def test__run_parallel_threadlimited(self, mock_gc, *args):
        mock_gc.return_value = 4
        jobs = [self.job, self.job, self.job, ]
        fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel(
            jobs, self.job_id, self.p_env, to_file=True,
            stdout_file=self.stdout, stderr_file=self.stderr,
            parallel_limit=2
        )

        job_list = []
        for subjob in (1, 2, 3):
            jobout = '.'.join((self.stdout, str(subjob)))
            joberr = '.'.join((self.stderr, str(subjob)))
            child_env = dict(self.p_env)
            child_env['JOB_ID'] = self.job_id
            child_env['SHELL_TASK_ID'] = subjob
            child_env['SHELL_TASK_FIRST'] = 1
            child_env['SHELL_TASK_LAST'] = 3
            child_env['SHELL_TASK_STEPSIZE'] = 1
            job_list.append([self.job, subjob, child_env, jobout, joberr])
            with open(jobout, 'r') as jout:
                joboutput = jout.read()
            with open(joberr, 'r') as jerr:
                joberror = jerr.read()
            self.assertEqual(
                joboutput,
                '''jobid:{0}
slots:{1}
taskid:{2}
start:{3}
end:{4}
step:{5}
'''.format(self.job_id, 1, subjob, 1, 3, 1))
            self.assertEqual(joberror, '')

    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell._get_cores',
        autospec=True)
    def test__run_parallel_spec(self, mock_gc, *args):
        mock_gc.return_value = 4
        jobs = [self.job, self.job, self.job, ]

        fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel(
            jobs, self.job_id, self.p_env,
            to_file=True,
            stdout_file=self.stdout, stderr_file=self.stderr,
            parallel_limit=2
        )

        job_list = []
        for subjob in (1, 2, 3):
            jobout = '.'.join((self.stdout, str(subjob)))
            joberr = '.'.join((self.stderr, str(subjob)))
            child_env = dict(self.p_env)
            child_env['JOB_ID'] = self.job_id
            child_env['SHELL_TASK_ID'] = subjob
            child_env['SHELL_TASK_FIRST'] = 1
            child_env['SHELL_TASK_LAST'] = 3
            child_env['SHELL_TASK_STEPSIZE'] = 1
            job_list.append([self.job, subjob, child_env, jobout, joberr])
            with open(jobout, 'r') as jout:
                joboutput = jout.read()
            with open(joberr, 'r') as jerr:
                joberror = jerr.read()
            self.assertEqual(
                joboutput,
                '''jobid:{0}
slots:{1}
taskid:{2}
start:{3}
end:{4}
step:{5}
'''.format(self.job_id, 1, subjob, 1, 3, 1))
            self.assertEqual(joberror, '')

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid', autospec=True)
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_job', autospec=True)
    def test_submit(self, mock__run_job, mock_getpid, *args):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))

        args = ['myjob', 'arg1', 'arg2', ]

        test_environ = {'AVAR': 'AVAL', }
        result_environ = dict(test_environ)
        result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
        result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
        result_environ['SHELL_NCPUS'] = '1'
        # result_environ['JOB_ID'] = str(mock_pid) - mocked so doesn't get set
        with patch.dict(
                'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                test_environ,
                clear=True):
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                command=args,
                job_name=jobname,
                queue="my.q",
                logdir=logdir)
            mock__run_job.assert_called_once_with(
                args,
                mock_pid,
                result_environ,
                True,
                logfile_stdout,
                logfile_stderr
            )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid', autospec=True)
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.sp.run', autospec=True)
    def test_quoted_arg_submit(
            self, mock_sp_run, mock_getpid, mock_bash, mock_rc):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        with tempfile.TemporaryDirectory() as tempdir:
            logdir = tempdir
            jobname = "myjob"

            args = [
                'myjob', '-arg1', '-arg2', '-arg3', "fprintf(1,'Hello World\n');"]  # noqa E501
            runner = [mock_bash.return_value, '-c', ]
            mock_sp_run.return_value = subprocess.CompletedProcess(
                runner + args, 0, '', '')

            test_environ = {'AVAR': 'AVAL', }
            result_environ = dict(test_environ)
            result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
            result_environ['SHELL_NCPUS'] = '1'
            result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
            result_environ['JOB_ID'] = str(mock_pid)
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    test_environ,
                    clear=True):

                fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                    command=args,
                    job_name=jobname,
                    queue="my.q",
                    logdir=logdir)
                mock_sp_run.assert_called_once_with(
                    runner + [" ".join(args)],
                    stdout=ANY, stderr=ANY,
                    universal_newlines=True,
                    env=result_environ
                )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid')
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel')
    def test_shell_parallel_submit(
            self, mock__run_parallel, mock_getpid, *args):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))
        ll_tests = ['mycommand arg1 arg2', 'mycommand2 arg3 arg4', ]

        with tempfile.TemporaryDirectory() as tempdir:
            job_file = os.path.join(tempdir, 'myjob')
            with open(job_file, mode='w') as jf:
                jf.writelines([a + '\n' for a in ll_tests])

            test_environ = {'AVAR': 'AVAL', }
            result_environ = dict(test_environ)
            result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
            result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
            result_environ['SHELL_NCPUS'] = '1'
            result_environ['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
            result_environ['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
            result_environ['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
            result_environ['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
            result_environ['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
            result_environ['FSLSUB_PARALLEL'] = '1'
            # result_environ['JOB_ID'] = str(mock_pid) -
            # mocked so doesn't get set
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    test_environ,
                    clear=True):
                fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                    command=[job_file],
                    job_name=jobname,
                    queue="my.q",
                    array_task=True,
                    logdir=logdir)
                mock__run_parallel.assert_called_once_with(
                    [shlex.split(a) for a in ll_tests],
                    mock_pid,
                    result_environ,
                    True,
                    logfile_stdout,
                    logfile_stderr
                )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid')
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel')
    def test_shell_parallel_submit_bash_singlelines(
            self, mock__run_parallel, mock_getpid, mock_bash, mock_rc):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))
        ll_tests = ['MYENVVAR=1234; sleep 1; mycommand arg1 arg2', 'MYENVVAR=5678; sleep 3; mycommand2 arg3 arg4', ]  # noqa E501
        ll_out = [[mock_bash.return_value, '-c', a] for a in ll_tests]
        with tempfile.TemporaryDirectory() as tempdir:
            job_file = os.path.join(tempdir, 'myjob')
            with open(job_file, mode='w') as jf:
                jf.writelines([a + '\n' for a in ll_tests])

            test_environ = {'AVAR': 'AVAL', }
            result_environ = dict(test_environ)
            result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
            result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
            result_environ['SHELL_NCPUS'] = '1'
            result_environ['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
            result_environ['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
            result_environ['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
            result_environ['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
            result_environ['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
            result_environ['FSLSUB_PARALLEL'] = '1'
            # result_environ['JOB_ID'] = str(mock_pid)
            # - mocked so doesn't get set
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    test_environ,
                    clear=True):
                fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                    command=[job_file],
                    job_name=jobname,
                    queue="my.q",
                    array_task=True,
                    logdir=logdir)
                mock__run_parallel.assert_called_once_with(
                    ll_out,
                    mock_pid,
                    result_environ,
                    True,
                    logfile_stdout,
                    logfile_stderr
                )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid')
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel')
    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell.method_config',
        autospec=True,
        return_value={
            'parallel_disable_matches': '*_gpu',
            'has_parallel_envs': False})
    def test_shell_parallel_submit_jname_disable(
            self, mock_mconf, mock__run_parallel, mock_getpid, *args):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))
        ll_tests = ['mycommand_gpu arg1 arg2',
                    'mycommand2 arg3 arg4',
                    '"mycommand3" arg5 arg6',
                    '"/spacy dir/mycommand4" arg5 arg6',
                    '/spacy\\ dir/mycommand4 arg5 arg6']

        with tempfile.TemporaryDirectory() as tempdir:
            job_file = os.path.join(tempdir, 'myjob')
            with open(job_file, mode='w') as jf:
                jf.writelines([a + '\n' for a in ll_tests])

            test_environ = {'AVAR': 'AVAL', }
            result_environ = dict(test_environ)
            result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
            result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
            result_environ['SHELL_NCPUS'] = '1'
            result_environ['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
            result_environ['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
            result_environ['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
            result_environ['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
            result_environ['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
            result_environ['FSLSUB_PARALLEL'] = '1'
            # result_environ['JOB_ID'] = str(mock_pid)
            # - mocked so doesn't get set
            with patch.dict(
                    'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                    test_environ,
                    clear=True):
                fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                    command=[job_file],
                    job_name=jobname,
                    queue="my.q",
                    array_task=True,
                    logdir=logdir)
                mock__run_parallel.assert_called_once_with(
                    [shlex.split(a) for a in ll_tests],
                    mock_pid,
                    result_environ,
                    True,
                    logfile_stdout,
                    logfile_stderr,
                    parallel_limit=1
                )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid')
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel')
    def test_shell_parallel_submit_spec(
            self, mock__run_parallel, mock_getpid, *args):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        spec = "4-8:4"
        njobs = 2
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))

        command = ['acmd', ]
        arraytask = True

        test_environ = {'AVAR': 'AVAL', }
        result_environ = dict(test_environ)
        result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
        result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
        result_environ['SHELL_NCPUS'] = '1'
        result_environ['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
        result_environ['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
        result_environ['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
        result_environ['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
        result_environ['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
        result_environ['FSLSUB_PARALLEL'] = '1'
        # result_environ['JOB_ID'] = str(mock_pid) - mocked so doesn't get set
        with patch.dict(
                'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                test_environ,
                clear=True):
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                command=command,
                job_name=jobname,
                queue="my.q",
                array_task=arraytask,
                array_specifier=spec,
                logdir=logdir)
            mock__run_parallel.assert_called_once_with(
                njobs * [command],
                mock_pid,
                result_environ,
                True,
                logfile_stdout,
                logfile_stderr,
                array_stride=4,
                array_start=4,
                array_end=8,
            )

    @patch('fsl_sub.plugins.fsl_sub_plugin_shell.os.getpid')
    @patch('fsl_sub.plugins.fsl_sub_plugin_shell._run_parallel')
    @patch(
        'fsl_sub.plugins.fsl_sub_plugin_shell.method_config',
        autospec=True,
        return_value={
            'parallel_disable_matches': '*_gpu',
            'has_parallel_envs': False})
    def test_shell_parallel_submit_spec_jname_disable(
            self, mock_mconf, mock__run_parallel, mock_getpid, *args):
        mock_pid = 12345
        mock_getpid.return_value = mock_pid
        logdir = "/tmp/logdir"
        jobname = "myjob"
        spec = "4-8:4"
        njobs = 2
        logfile_stdout = os.path.join(
            logdir, jobname + ".o" + str(mock_pid))
        logfile_stderr = os.path.join(
            logdir, jobname + ".e" + str(mock_pid))

        command = ['acmd_gpu', ]
        arraytask = True

        test_environ = {'AVAR': 'AVAL', }
        result_environ = dict(test_environ)
        result_environ['FSLSUB_JOBID_VAR'] = 'JOB_ID'
        result_environ['FSLSUB_NSLOTS'] = 'SHELL_NCPUS'
        result_environ['SHELL_NCPUS'] = '1'
        result_environ['FSLSUB_ARRAYTASKID_VAR'] = 'SHELL_TASK_ID'
        result_environ['FSLSUB_ARRAYSTARTID_VAR'] = 'SHELL_TASK_FIRST'
        result_environ['FSLSUB_ARRAYENDID_VAR'] = 'SHELL_TASK_LAST'
        result_environ['FSLSUB_ARRAYSTEPSIZE_VAR'] = 'SHELL_TASK_STEPSIZE'
        result_environ['FSLSUB_ARRAYCOUNT_VAR'] = 'SHELL_ARRAYCOUNT'
        result_environ['FSLSUB_PARALLEL'] = '1'
        # result_environ['JOB_ID'] = str(mock_pid) - mocked so doesn't get set
        with patch.dict(
                'fsl_sub.plugins.fsl_sub_plugin_shell.os.environ',
                test_environ,
                clear=True):
            fsl_sub.plugins.fsl_sub_plugin_shell.submit(
                command=command,
                job_name=jobname,
                queue="my.q",
                array_task=arraytask,
                array_specifier=spec,
                logdir=logdir)
            mock__run_parallel.assert_called_once_with(
                njobs * [command],
                mock_pid,
                result_environ,
                True,
                logfile_stdout,
                logfile_stderr,
                array_start=4,
                array_end=8,
                array_stride=4,
                parallel_limit=1
            )


if __name__ == '__main__':
    unittest.main()
