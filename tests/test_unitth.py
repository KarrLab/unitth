""" Tests unitth

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-08-04
:Copyright: 2016, Karr Lab
:License: MIT
"""

from past import autotranslate
from nose2unitth.core import Converter as nose2unitth
from junit2htmlreport.parser import Junit as JunitParser
from unitth.core import UnitTH
import shutil
import subprocess
import os
import tempfile
import unittest


class TestUnitTH(unittest.TestCase):
    TEST_API = True
    TEST_CLI = False
    PROJECT_NAME = 'Karr-Lab-build-utils'
    COVERALLS_REPO_TOKEN = ''

    def setUp(self):
        report_dir = tempfile.mkdtemp()

        nose_dir = os.path.join(report_dir, 'nose')
        unitth_dir = os.path.join(report_dir, 'unitth')
        html_dir = os.path.join(report_dir, 'html')
        os.mkdir(nose_dir)
        os.mkdir(unitth_dir)
        os.mkdir(html_dir)

        subprocess.check_call(['nosetests', 'tests/test_unitth.py:TestDummy.test_dummy_test',
                               '--with-xunit', '--xunit-file', os.path.join(nose_dir, '1.xml')])
        shutil.copyfile(os.path.join(nose_dir, '1.xml'), os.path.join(nose_dir, '2.xml'))

        nose2unitth.run(os.path.join(nose_dir, '1.xml'), os.path.join(unitth_dir, '1'))
        nose2unitth.run(os.path.join(nose_dir, '2.xml'), os.path.join(unitth_dir, '2'))

        with open(os.path.join(os.path.join(unitth_dir, '1', 'index.html')), 'w') as html_file:
            html_file.write(JunitParser(os.path.join(nose_dir, '1.xml')).html())
        with open(os.path.join(os.path.join(unitth_dir, '2', 'index.html')), 'w') as html_file:
            html_file.write(JunitParser(os.path.join(nose_dir, '2.xml')).html())

        self._report_dir = report_dir
        self._nose_dir = nose_dir
        self._unitth_dir = unitth_dir
        self._html_dir = html_dir

    def tearDown(self):
        shutil.rmtree(self._report_dir)

    def test_api(self):
        UnitTH.run(os.path.join(self._unitth_dir, '*'), xml_report_filter='', html_report_dir=self._html_dir)
        self.assertTrue(os.path.isfile(os.path.join(self._html_dir, 'index.html')))

    def test_cli(self):
        subprocess.check_call(['python', 'unitth/bin/run.py', 
            os.path.join(self._unitth_dir, '*'), 
            '--xml_report_filter', '', 
            '--html_report_dir', self._html_dir,
            ])
        self.assertTrue(os.path.isfile(os.path.join(self._html_dir, 'index.html')))


class TestDummy(object):

    def test_dummy_test(self):
        pass
