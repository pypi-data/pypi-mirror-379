#!/usr/bin/env python
from importlib.resources import files
import unittest
import fsl_sub.config
import copy
import os
import shutil
import subprocess
import tempfile
import uuid

from ruamel.yaml import YAML
from unittest.mock import (patch, mock_open)

from fsl_sub.exceptions import BadConfiguration


class TestConfig(unittest.TestCase):
    def test_get_option(self):
        options = {'testopt': True, }

        self.assertTrue(
            fsl_sub.config.get_option('testopt', options)
        )
        options = {'testopt': 'true', }
        self.assertEqual(
            'true',
            fsl_sub.config.get_option('testopt', options)
        )
        self.assertTrue(
            fsl_sub.config.get_option('testopt', options, boolean=True)
        )
        options = {'testopt': 'false', }
        self.assertFalse(
            fsl_sub.config.get_option('testopt', options, boolean=True)
        )
        options = {'testopt': '1', }
        self.assertTrue(
            fsl_sub.config.get_option('testopt', options, boolean=True)
        )
        options = {'testopt': '0', }
        self.assertFalse(
            fsl_sub.config.get_option('testopt', options, boolean=True)
        )

        self.assertIsNone(
            fsl_sub.config.get_option('anotheropt', options)
        )

        self.assertTrue(
            fsl_sub.config.get_option('anotheropt', options, default=True)
        )

        self.assertRaises(
            ValueError,
            fsl_sub.config.get_option,
            'anotheropt', options, boolean=True
        )

        with patch.dict(
                'fsl_sub.config.os.environ',
                {'FSLSUB_TESTOPT': '1'}):

            self.assertTrue(
                fsl_sub.config.get_option(
                    'testopt', options, boolean=True)
            )
            options = {'testopt': '0', }
            self.assertTrue(
                fsl_sub.config.get_option(
                    'testopt', options, boolean=True))
            self.assertFalse(
                fsl_sub.config.get_option(
                    'testopt', options, boolean=True, prefer_cmdline=True))

        with patch.dict(
                'fsl_sub.config.os.environ',
                {'FSLSUB_TESTOPT': 'MYVALUE'}):

            self.assertEqual(
                'MYVALUE',
                fsl_sub.config.get_option(
                    'testopt', options)
            )

    @patch('fsl_sub.config.os.path.expanduser', autospec=True)
    def test_find_config_file(
            self, mock_expanduser):
        test_dir = tempfile.mkdtemp()
        try:
            test_file = os.path.join(test_dir, '.fsl_sub.yml')
            with open(test_file, 'w') as tf:
                tf.write('something')

            with patch.dict(
                    'fsl_sub.config.os.environ',
                    {'RANDOMENV': 'A', },
                    clear=True):
                with self.subTest('Expand user'):
                    mock_expanduser.return_value = test_dir
                    self.assertEqual(
                        fsl_sub.config.find_config_file(),
                        test_file
                    )
            os.unlink(test_file)
            test_file = os.path.join(test_dir, 'fsl_sub.yml')
            with open(test_file, 'w') as tf:
                tf.write('something')
            with self.subTest('Environment variable'):

                with patch.dict(
                        'fsl_sub.config.os.environ',
                        {'FSLSUB_CONF': test_file, },
                        clear=True):
                    self.assertEqual(
                        fsl_sub.config.find_config_file(),
                        test_file
                    )
            os.unlink(test_file)
            fsl_dir = os.path.join(test_dir, 'etc', 'fslconf')
            os.makedirs(fsl_dir)
            test_file = os.path.join(fsl_dir, 'fsl_sub.yml')
            with open(test_file, 'w') as tf:
                tf.write('something')
            with patch.dict(
                    'fsl_sub.config.os.environ',
                    {'FSLDIR': test_dir, },
                    clear=True):
                with self.subTest('FSLDIR'):
                    self.assertEqual(
                        fsl_sub.config.find_config_file(),
                        os.path.realpath(test_file)
                    )
            shutil.rmtree(os.path.join(test_dir, 'etc'))

            with self.subTest('Missing configuration'):
                with patch(
                        'fsl_sub.config.os.path.exists',
                        return_value=False):
                    self.assertRaises(
                        fsl_sub.config.MissingConfiguration,
                        fsl_sub.config.find_config_file
                    )

            with self.subTest('No FSLDIR'):
                with patch.dict(
                        'fsl_sub.config.os.environ',
                        clear=True):
                    location = str(files('fsl_sub').joinpath(
                        'plugins', 'fsl_sub_shell.yml'))

                    self.assertEqual(
                        fsl_sub.config.find_config_file(),
                        location
                    )
        finally:
            shutil.rmtree(test_dir)

    @patch('fsl_sub.config.get_plugin_default_conf')
    @patch('fsl_sub.config._internal_config_file')
    @patch('fsl_sub.config.get_plugin_queue_defs', return_value='')
    def test_example_conf(self, mock_gpqd, mock_dcf, mock_gpe):
        self.maxDiff = None
        yaml = YAML()
        base_cpopt = '''baseopt: bits
'''
        base_config = '''modulecmd: false
thread_control:
  - OMP_NUM_THREADS
method_opts: {}
queues: {}
coproc_opts: {}
'''
        coproc_config = '''---
coproc_opts:
  cuda:
    resource: somethingelse
'''
        def_coproc_config = '''---
coproc_opts:
  cuda:
    ''' + base_cpopt
        queue_config = '''---
queues:
  short.q:
    runtime: 100
'''
        method_config = (
            '''method: shell
method_opts:
  shell:
    queues: false''',
            '''method: sge
method_opts:
  sge:
    has_parallel_envs: false
    queues: true''', )
        merged_method_config = '''method_opts:
  shell:
    queues: false
  sge:
    has_parallel_envs: false
    queues: true'''
        expected_output = (
            "---\nmethod: sge\n"
            + base_config.replace(
                'method_opts: {}\n', '').replace(
                    'queues: {}\n', '').replace(
                        'coproc_opts: {}\n', '')
            + merged_method_config + '\n'
            + coproc_config.replace(
                '---\n', '').replace(
                    'cuda:\n', 'cuda:\n    ' + base_cpopt)
            + queue_config.replace('---\n', '')
        )
        mock_gpqd.return_value = ''
        with self.subTest('Single quoted method'):
            with tempfile.NamedTemporaryFile(mode='w') as ntf:
                ntf.write("---\nmethod: 'shell'\n" + base_config)
                ntf.flush()
                with tempfile.NamedTemporaryFile(mode='w') as ntf_cp:
                    ntf_cp.write(coproc_config)
                    ntf_cp.flush()
                    with tempfile.NamedTemporaryFile(mode='w') as ntf_cq:
                        ntf_cq.write(queue_config)
                        ntf_cq.flush()
                        with tempfile.NamedTemporaryFile(mode='w') as ntf_dcp:
                            ntf_dcp.write(def_coproc_config)
                            ntf_dcp.flush()
                            mock_dcf.side_effect = (
                                ntf.name, ntf_dcp.name,
                                ntf_cq.name, ntf_cp.name)
                            mock_gpe.side_effect = method_config
                            c_od = fsl_sub.config.example_config(method='sge')
                            e_od = yaml.load(expected_output)
                            self.assertEqual(c_od, e_od)
                            mock_dcf.reset_mock(
                                return_value=True, side_effect=True)
                            mock_gpe.reset_mock(
                                return_value=True, side_effect=True)

        with self.subTest('Double quoted method'):
            with tempfile.NamedTemporaryFile(mode='w') as ntf:
                ntf.write('---\nmethod: "shell"\n' + base_config)
                ntf.flush()
                with tempfile.NamedTemporaryFile(mode='w') as ntf_cp:
                    ntf_cp.write(coproc_config)
                    ntf_cp.flush()
                    with tempfile.NamedTemporaryFile(mode='w') as ntf_cq:
                        ntf_cq.write(queue_config)
                        ntf_cq.flush()
                        with tempfile.NamedTemporaryFile(mode='w') as ntf_dcp:
                            ntf_dcp.write(def_coproc_config)
                            ntf_dcp.flush()
                            mock_dcf.side_effect = (
                                ntf.name, ntf_dcp.name,
                                ntf_cq.name, ntf_cp.name)
                            mock_gpe.side_effect = method_config
                            c_od = fsl_sub.config.example_config(method='sge')
                            e_od = yaml.load(expected_output)
                            self.assertEqual(c_od, e_od)
                            mock_dcf.reset_mock(
                                return_value=True, side_effect=True)
                            mock_gpe.reset_mock(
                                return_value=True, side_effect=True)

        with self.subTest('unquoted quoted method'):
            with tempfile.NamedTemporaryFile(mode='w') as ntf:
                ntf.write('---\nmethod: shell\n' + base_config)
                ntf.flush()
                with tempfile.NamedTemporaryFile(mode='w') as ntf_cp:
                    ntf_cp.write(coproc_config)
                    ntf_cp.flush()
                    with tempfile.NamedTemporaryFile(mode='w') as ntf_cq:
                        ntf_cq.write(queue_config)
                        ntf_cq.flush()
                        with tempfile.NamedTemporaryFile(mode='w') as ntf_dcp:
                            ntf_dcp.write(def_coproc_config)
                            ntf_dcp.flush()
                            mock_dcf.side_effect = (
                                ntf.name, ntf_dcp.name,
                                ntf_cq.name, ntf_cp.name)
                            mock_gpe.side_effect = method_config
                            c_od = fsl_sub.config.example_config(method='sge')
                            e_od = yaml.load(expected_output)
                            self.assertEqual(c_od, e_od)
                            mock_dcf.reset_mock(
                                return_value=True, side_effect=True)
                            mock_gpe.reset_mock(
                                return_value=True, side_effect=True)

        with self.subTest('Queue capture'):
            q_def = '''queues:
  a.q:
    time: 1'''
            qc_expected_output = (
                "---\nmethod: 'sge'\n"
                + base_config.replace(
                    'method_opts: {}\n', '').replace(
                        'queues: {}\n', '').replace(
                            'coproc_opts: {}\n', '')
                + merged_method_config + '\n'
                + coproc_config.replace(
                    '---\n', '').replace(
                        'cuda:\n', 'cuda:\n    ' + base_cpopt)
                + q_def
            )
            mock_gpqd.return_value = YAML().load(q_def)
            with tempfile.NamedTemporaryFile(mode='w') as ntf:
                ntf.write("---\nmethod: 'shell'\n" + base_config)
                ntf.flush()
                with tempfile.NamedTemporaryFile(mode='w') as ntf_cp:
                    ntf_cp.write(coproc_config)
                    ntf_cp.flush()
                    with tempfile.NamedTemporaryFile(mode='w') as ntf_cq:
                        ntf_cq.write(queue_config)
                        ntf_cq.flush()
                        with tempfile.NamedTemporaryFile(mode='w') as ntf_dcp:
                            ntf_dcp.write(def_coproc_config)
                            ntf_dcp.flush()
                            mock_dcf.side_effect = (
                                ntf.name, ntf_dcp.name,
                                ntf_cq.name, ntf_cp.name)
                            mock_gpe.side_effect = method_config
                            c_od = fsl_sub.config.example_config(method='sge')
                            e_od = yaml.load(qc_expected_output)
                            self.assertEqual(c_od, e_od)
                            mock_dcf.reset_mock(
                                return_value=True, side_effect=True)
                            mock_gpe.reset_mock(
                                return_value=True, side_effect=True)

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={'bdict': "somevalue", })
    @patch('fsl_sub.config.find_config_file', autospec=True)
    def test_read_config_merge(self, mock_find_config_file, mock_ldc):
        fsl_sub.config.read_config.cache_clear()
        example_yaml = '''
adict:
    alist:
        - 1
        - 2
    astring: hello
'''
        mock_find_config_file.return_value = '/etc/fsl_sub.conf'
        with patch(
                'fsl_sub.config.open',
                unittest.mock.mock_open(read_data=example_yaml)) as m:
            self.assertDictEqual(
                fsl_sub.config.read_config(),
                {
                    'adict': {
                        'alist': [1, 2],
                        'astring': 'hello',
                    },
                    'bdict': 'somevalue',
                }
            )
            m.assert_called_once_with('/etc/fsl_sub.conf', 'r')

    @patch('fsl_sub.config._internal_config_file', autospec=True)
    @patch('fsl_sub.config.get_plugin_default_conf', autospec=True)
    @patch('fsl_sub.config.available_plugins', autospec=True)
    def test_load_default_config(self, mock_ap, mock_gpec, mock__icf):
        base_conf = '''---
method: 'shell'
thread_control: []
method_opts: {}
coproc_opts: {}
queues: {}
'''
        plugins = [
            '''---
method_opts:
  shell:
    queues: False
''',
            '''---
method: 'sge'
method_opts:
  sge:
    has_parallel_envs: False
    queues: True
''', ]
        expected_config = {
            'method': 'shell',
            'thread_control': [],
            'method_opts': {
                'shell': {
                    'queues': False,
                },
                'sge': {
                    'queues': True,
                    'has_parallel_envs': False,
                },
            },
            'coproc_opts': {},
            'queues': {},
        }
        with tempfile.NamedTemporaryFile(mode='w') as ntf:
            ntf.write(base_conf)
            ntf.flush()
            mock_ap.return_value = ['shell', 'sge', ]
            mock__icf.return_value = ntf.name
            mock_gpec.side_effect = plugins
            self.assertDictEqual(
                fsl_sub.config.load_default_config(),
                expected_config)
            mock_ap.reset_mock()
            mock__icf.reset_mock()
            mock_gpec.reset_mock()

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.find_config_file', autospec=True)
    def test_read_config(self, mock_find_config_file, mock_ldc):
        with self.subTest("Test good read"):
            fsl_sub.config.read_config.cache_clear()
            example_yaml = '''
adict:
    alist:
        - 1
        - 2
    astring: hello
'''
            mock_find_config_file.return_value = '/etc/fsl_sub.conf'
            with patch(
                    'fsl_sub.config.open',
                    unittest.mock.mock_open(read_data=example_yaml)) as m:
                self.assertDictEqual(
                    fsl_sub.config.read_config(),
                    {'adict': {
                        'alist': [1, 2],
                        'astring': 'hello',
                    }}
                )
                m.assert_called_once_with('/etc/fsl_sub.conf', 'r')
        with self.subTest("Test bad read"):
            fsl_sub.config.read_config.cache_clear()
            bad_yaml = "unbalanced: ]["
            with patch(
                    'fsl_sub.config.open',
                    unittest.mock.mock_open(read_data=bad_yaml)) as m:
                self.assertRaises(
                    fsl_sub.config.BadConfiguration,
                    fsl_sub.config.read_config)
        with self.subTest("CUDA Warning"):
            fsl_sub.config.read_config.cache_clear()
            missing_cuda = """
coproc_opts:
    acoproc:
        setting: value
"""
            with patch(
                    'fsl_sub.config.open',
                    unittest.mock.mock_open(read_data=missing_cuda)) as m:

                with self.assertWarns(Warning) as cm:
                    self.assertEqual(
                        fsl_sub.config.read_config(),
                        {'coproc_opts': {'acoproc': {'setting': 'value'}}}
                    )
                self.assertEqual(
                    str(cm.warning),
                    '(cuda) Coprocessors configured but no "cuda" '
                    'coprocessor found. FSL tools will not be able to '
                    'autoselect CUDA versions of software.'
                )

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.find_config_file', autospec=True)
    def test_read_user_config_overrides(self, mock_find_config_file, mock_ldc):
        fsl_sub.config.read_config.cache_clear()
        example_yaml = '''
adict:
    alist:
        - 1
        - 2
    astring: hello
'''
        user_over_yaml = '''
adict:
    alist:
        - 3
'''
        mock_find_config_file.return_value = '/etc/fsl_sub.conf'
        mock_fhs = [
            mock_open(read_data=example_yaml).return_value,
            mock_open(read_data=user_over_yaml).return_value,
        ]
        mock_opener = mock_open()
        mock_opener.side_effect = mock_fhs

        with patch('fsl_sub.config.os.path.exists', return_value=True):
            with patch('fsl_sub.config.open', mock_opener) as m:
                self.assertDictEqual(
                    fsl_sub.config.read_config(),
                    {'adict': {
                        'alist': [3, ],
                        'astring': 'hello',
                    }}
                )
                m.assert_called_with(
                    os.path.join(
                        os.path.expanduser("~"), '.fsl_sub.yml'), 'r')

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.find_config_file', autospec=True)
    def test_read_user_config_nested_overrides(
            self, mock_find_config_file, mock_ldc):
        fsl_sub.config.read_config.cache_clear()
        example_yaml = '''
adict:
    akey:
        alist:
            - 1
            - 2
        blist:
            - 3
            - 4
    bkey: hello
'''
        user_over_yaml = '''
adict:
    akey:
        alist:
            - 5
            - 6
'''
        mock_find_config_file.return_value = '/etc/fsl_sub.conf'
        mock_fhs = [
            mock_open(read_data=example_yaml).return_value,
            mock_open(read_data=user_over_yaml).return_value,
        ]
        mock_opener = mock_open()
        mock_opener.side_effect = mock_fhs

        with patch('fsl_sub.config.os.path.exists', return_value=True):
            with patch('fsl_sub.config.open', mock_opener) as m:
                self.assertDictEqual(
                    fsl_sub.config.read_config(),
                    {'adict': {
                        'akey': {'alist': [5, 6, ], 'blist': [3, 4, ], },
                        'bkey': 'hello',
                    }}
                )
                m.assert_called_with(
                    os.path.join(
                        os.path.expanduser("~"),
                        '.fsl_sub.yml'), 'r')

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.read_config', autospec=True)
    def test_method_config(self, mock_read_config, mock_ldc):

        with self.subTest('Test 1'):
            mock_read_config.return_value = {
                'method_opts': {'method': 'config', }, }
            self.assertEqual('config', fsl_sub.config.method_config('method'))

        with self.subTest('Test 2'):
            self.assertRaises(
                TypeError,
                fsl_sub.config.method_config
            )

        with self.subTest('Test 3'):
            mock_read_config.return_value = {
                'method_o': {'method': 'config', }, }
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.method_config('method')
            self.assertEqual(
                me.exception.args[0],
                "Unable to find method configuration dictionary")

        with self.subTest('Test 4'):
            mock_read_config.return_value = {
                'method_opts': {'method': 'config', }, }
            self.assertEqual('config', fsl_sub.config.method_config('method'))
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.method_config('method2')
            self.assertEqual(
                me.exception.args[0],
                "Unable to find configuration for method2")

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.read_config', autospec=True)
    def test_coprocessor_config(self, mock_read_config, mock_ldc):

        with self.subTest('Test 1'):
            mock_read_config.return_value = {
                'coproc_opts': {'cuda': 'option', }, }
            self.assertEqual(
                'option', fsl_sub.config.coprocessor_config('cuda'))

        with self.subTest('Test 2'):
            self.assertRaises(
                TypeError,
                fsl_sub.config.coprocessor_config
            )

        with self.subTest('Test 3'):
            mock_read_config.return_value = {
                'coproc_o': {'cuda': 'option', }, }
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.coprocessor_config('cuda')
            self.assertEqual(
                me.exception.args[0],
                "Unable to find coprocessor configuration dictionary")

        with self.subTest('Test 4'):
            mock_read_config.return_value = {
                'coproc_opts': {'cuda': 'option', }, }
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.coprocessor_config('phi')
            self.assertEqual(
                me.exception.args[0],
                "Unable to find configuration for phi")

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.read_config', autospec=True)
    def test_queue_config(self, mock_read_config, mock_ldc):

        mock_read_config.return_value = {
            'queues': {'short.q': 'option', }, }
        with self.subTest('Test 1'):
            self.assertEqual(
                'option', fsl_sub.config.queue_config('short.q'))

        with self.subTest('Test 2'):
            self.assertDictEqual(
                {'short.q': 'option', },
                fsl_sub.config.queue_config())

        with self.subTest('Test 3'):
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.queue_config('long.q')
            self.assertEqual(
                me.exception.args[0],
                "Unable to find definition for queue long.q")

        with self.subTest('Test 4'):
            mock_read_config.return_value = {
                'q': {'short.q': 'option', }, }
            with self.assertRaises(fsl_sub.config.BadConfiguration) as me:
                fsl_sub.config.queue_config()
            self.assertEqual(
                me.exception.args[0],
                "Unable to find queue definitions")

    @patch(
        'fsl_sub.config.load_default_config',
        autospec=True,
        return_value={})
    @patch('fsl_sub.config.read_config', autospec=True)
    def test_uses_projects(self, mock_read_config, mock_ldc):

        with self.subTest('Test 1'):
            mock_read_config.return_value = {
                'method': 'method',
                'method_opts': {'method': {'projects': False, }, }, }
            self.assertFalse(fsl_sub.config.uses_projects())

        with self.subTest('Test 2'):
            mock_read_config.return_value = {
                'method': 'method',
                'method_opts': {'method': {'projects': True, }, }, }
            self.assertTrue(fsl_sub.config.uses_projects())

    @patch('fsl_sub.config.read_config', autospec=True)
    def test_has_queues(self, mock_rc):
        with self.subTest("No queues"):
            mock_rc.return_value = {
                'method': 'shell',
                'method_opts': {
                    'shell': {'queues': False, },
                },
                'queues': {}
            }
            self.assertFalse(fsl_sub.config.has_queues())
            self.assertFalse(fsl_sub.config.has_queues('shell'))
            self.assertRaises(
                fsl_sub.config.BadConfiguration,
                fsl_sub.config.has_queues,
                'nonsense'
            )
        with self.subTest("Has queues/not configured"):
            mock_rc.return_value = {
                'method': 'shell',
                'method_opts': {
                    'shell': {'queues': True, },
                },
                'queues': {}
            }
            self.assertFalse(fsl_sub.config.has_queues())
            self.assertFalse(fsl_sub.config.has_queues('shell'))
        with self.subTest("Has queues and configured"):
            mock_rc.return_value = {
                'method': 'shell',
                'method_opts': {
                    'shell': {'queues': True, },
                },
                'queues': {
                    'queue1': {},
                },
            }
            self.assertTrue(fsl_sub.config.has_queues())
            self.assertTrue(fsl_sub.config.has_queues('shell'))

    @patch('fsl_sub.config.get_plugin_already_queued', autospec=True)
    @patch('fsl_sub.config.read_config', autospec=True)
    @patch('fsl_sub.config.sp.run', autospec=True)
    @patch('fsl_sub.config.which', autospec=True)
    def test_has_coprocessor(self, mock_which, mock_spr, mock_rc, mock_gpaq):
        with self.subTest("No coprocessor"):
            mock_gpaq.return_value = False
            mock_rc.return_value = {
                'method': 'something',
                'queues': {'aq': {}, },
                'coproc_opts': {},
            }
            self.assertFalse(fsl_sub.config.has_coprocessor('cuda'))
        with self.subTest("Has coprocessor definition - no queue"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = False
            mock_spr.return_value = subprocess.CompletedProcess(
                ['/usr/bin/nvidia-smi'], returncode=0
            )
            mock_which.return_value = '/usr/bin/nvidia-smi'
            mock_rc.return_value = {
                'method': 'something',
                'queues': {'aq': {}, },
                'coproc_opts': {'cuda': {'presence_test': 'nvidia-smi', }, },
            }
            self.assertFalse(fsl_sub.config.has_coprocessor('cuda'))
        with self.subTest("Has coprocessor definition - with queue"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = False
            mock_spr.return_value = subprocess.CompletedProcess(
                ['/usr/bin/nvidia-smi'], returncode=0
            )
            mock_which.return_value = '/usr/bin/nvidia-smi'
            mock_rc.return_value = {
                'method': 'something',
                'queues': {'aq': {'copros': {'cuda': {}, }, }, },
                'coproc_opts': {'cuda': {'presence_test': 'nvidia-smi', }, },
            }
            self.assertTrue(fsl_sub.config.has_coprocessor('cuda'))
        with self.subTest("Already queued + CUDA"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = True
            self.assertTrue(fsl_sub.config.has_coprocessor('cuda'))
            mock_which.assert_called_once_with(
                'nvidia-smi'
            )
            mock_spr.assert_called_once_with(
                ['/usr/bin/nvidia-smi']
            )
        with self.subTest("Shell method + CUDA"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = False
            mock_rc.return_value = {
                'method': 'shell',
                'queues': {},
                'coproc_opts': {'cuda': {'presence_test': 'nvidia-smi'}, },
            }
            self.assertTrue(fsl_sub.config.has_coprocessor('cuda'))
            mock_which.assert_called_once_with(
                'nvidia-smi'
            )
            mock_spr.assert_called_once_with(
                ['/usr/bin/nvidia-smi']
            )
        with self.subTest("Shell method - CUDA devices not found"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = False
            mock_rc.return_value = {
                'method': 'shell',
                'queues': {},
                'coproc_opts': {'cuda': {'presence_test': 'nvidia-smi'}, },
            }
            mock_spr.return_value = subprocess.CompletedProcess(
                ['/usr/bin/nvidia-smi'], returncode=6
            )
            self.assertFalse(fsl_sub.config.has_coprocessor('cuda'))
            mock_spr.assert_called_once_with(
                ['/usr/bin/nvidia-smi']
            )
            mock_which.assert_called_once_with(
                'nvidia-smi'
            )
        with self.subTest("Shell method - no SMI"):
            mock_spr.reset_mock()
            mock_which.reset_mock()
            mock_gpaq.return_value = False
            mock_rc.return_value = {
                'method': 'shell',
                'queues': {},
                'coproc_opts': {'cuda': {'presence_test': 'nvidia-smi'}, },
            }
            mock_which.return_value = None
            self.assertFalse(fsl_sub.config.has_coprocessor('cuda'))
            mock_which.assert_called_once_with(
                'nvidia-smi'
            )


class Test_Validate_Config(unittest.TestCase):
    def setUp(self) -> None:
        self.config = {
            'method': 'sge',
            'method_opts': {
                'sge': {
                    'queues': True,
                    'large_job_split_pe': 'openmp',
                    'has_parallel_envs': True,
                },
            },
            'queues': {
                'aq': {
                    'map_ram': True,
                    'parallel_envs': ['openmp', ]
                }
            }
        }
        return super().setUp()

    def test_validate_config(self):
        with self.subTest('Valid map_ram/PE config on SGE'):
            tconfig = copy.deepcopy(self.config)
            fsl_sub.config.validate_config(tconfig)

        with self.subTest('Valid map_ram/PE config on SGE - multiple queues'):
            tconfig = copy.deepcopy(self.config)
            tconfig['method_opts'][tconfig[
                'method']][
                    'has_parallel_envs'] = True
            tconfig['queues']['bq'] = {
                'map_ram': True,
                'parallel_envs': ['openmp', ]
            }
            fsl_sub.config.validate_config(tconfig)

        with self.subTest(
                'Valid map_ram/PE config on SGE - ' +
                'multiple queues PE on second'):
            tconfig = copy.deepcopy(self.config)
            tconfig['method_opts'][
                tconfig['method']][
                    'has_parallel_envs'] = True
            tconfig['queues']['bq'] = {
                'map_ram': True,
                'parallel_envs': ['openmp', ]
            }
            tconfig['queues']['aq'] = {
                'map_ram': False,
            }
            fsl_sub.config.validate_config(tconfig)

        with self.subTest('map_ram but no PEs'):
            tconfig = copy.deepcopy(self.config)
            del tconfig['queues']['aq']['parallel_envs']
            del tconfig['method_opts'][tconfig['method']]['has_parallel_envs']
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "Queue aq has map_ram set to True but no parallel" +
                " environments listed"
            )

        with self.subTest(
                'Miss-matched large_job_split_pe/PE config on SGE (1)'):
            tconfig = copy.deepcopy(self.config)
            tconfig['queues']['aq']['parallel_envs'] = ['smp', ]
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "openmp not found in configured parallel environments for aq"
            )

        with self.subTest(
                'Miss-matched large_job_split_pe/PE config on SGE (2)'):
            tconfig = copy.deepcopy(self.config)
            tconfig['method_opts']['sge']['large_job_split_pe'] = 'smp'
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "smp not found in configured parallel environments for aq"
            )

        with self.subTest('large_job_split_pe not set'):
            tconfig = copy.deepcopy(self.config)
            del tconfig['method_opts']['sge']['large_job_split_pe']
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "Queue aq has map_ram set to True but large_job_split_pe " +
                "is not set"
            )

        with self.subTest('Legacy ll_env config'):
            tconfig = copy.deepcopy(self.config)
            del tconfig['method_opts'][tconfig['method']]['has_parallel_envs']

            with self.assertWarns(Warning) as cm:
                fsl_sub.config.validate_config(tconfig)

            self.assertEqual(
                str(cm.warning),
                "Configuration should be updated, queues have parallel " +
                "environments defined but method options for sge is " +
                "missing has_parallel_envs: true"
            )

        with self.subTest('Legacy ll_env config - SLURM'):
            tconfig = copy.deepcopy(self.config)
            del tconfig['queues']['aq']['parallel_envs']
            del tconfig['method_opts']['sge']['large_job_split_pe']
            del tconfig['queues']['aq']['map_ram']
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "Method options for sge specifies has_parallel_envs: true " +
                "but no queues have parallel environments defined"
            )

        with self.subTest('ModuleCMD not existing'):
            tconfig = copy.deepcopy(self.config)
            tempdir = tempfile.gettempdir()
            unique_filename = os.path.join(tempdir, str(uuid.uuid4()))

            tconfig['modulecmd'] = unique_filename
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "modulecmd is set to {0}, ".format(unique_filename) +
                "but this either does not exist or is not an executable"
            )

        with self.subTest('ModuleCMD not executable existing'):
            tconfig = copy.deepcopy(self.config)
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                pass

            tconfig['modulecmd'] = fp.name
            with self.assertRaises(BadConfiguration) as em:
                fsl_sub.config.validate_config(tconfig)
            self.assertEqual(
                str(em.exception),
                "modulecmd is set to {0}, ".format(fp.name) +
                "but this either does not exist or is not an executable"
            )
            os.unlink(fp.name)


if __name__ == '__main__':
    unittest.main()
