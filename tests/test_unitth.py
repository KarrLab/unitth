""" Tests unitth

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-08-04
:Copyright: 2016, Karr Lab
:License: MIT
"""

from nose2unitth.core import Converter as nose2unitth
from junit2htmlreport.parser import Junit as JunitParser
from unitth.core import UnitTH
from unitth.__main__ import App as UnitThCli
import mock
import nose
import shutil
import os
import sys
import tempfile
import unittest
import unitth


class TestUnitTH(unittest.TestCase):

    def setUp(self):
        report_dir = tempfile.mkdtemp()

        nose_dir = os.path.join(report_dir, 'nose')
        unitth_dir = os.path.join(report_dir, 'unitth')
        html_dir = os.path.join(report_dir, 'html')
        os.mkdir(nose_dir)
        os.mkdir(unitth_dir)
        os.mkdir(html_dir)

        if not nose.run(argv=['nosetests', 'tests/test_unitth.py:TestDummy.test_dummy_test',
                              '--with-xunit', '--xunit-file', os.path.join(nose_dir, '1.xml')]):
            sys.exit(1)
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
        self.assertTrue(os.path.isfile(os.path  .join(self._html_dir, 'index.html')))

    def test_cli(self):
        argv = [
            os.path.join(self._unitth_dir, '*'),
            '--xml-report-filter', '',
            '--html-report-dir', self._html_dir,
        ]
        with UnitThCli(argv=argv) as app:
            app.run()

        self.assertTrue(os.path.isfile(os.path.join(self._html_dir, 'index.html')))

    def test_raw_cli(self):
        with mock.patch('sys.argv', ['unitth', '--help']):
            with self.assertRaises(SystemExit) as context:
                unitth.__main__.main()
                self.assertRegex(context.Exception, 'usage: unitth')

    def test_low_memory(self):
        UnitTH.run(os.path.join(self._unitth_dir, '*'), xml_report_filter='', html_report_dir=self._html_dir,
                   initial_java_heap_size='32m', maximum_java_heap_size='64m')
        self.assertTrue(os.path.isfile(os.path  .join(self._html_dir, 'index.html')))

    def test_api(self):
        self.assertIsInstance(unitth.UnitTH, type)


class TestDummy(object):

    def test_dummy_test(self):
        pass
