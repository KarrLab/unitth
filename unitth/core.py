""" UnitTH python interface

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-08-04
:Copyright: 2016, Karr Lab
:License: MIT
"""

from pkg_resources import resource_filename
import subprocess


class UnitTH(object):
    """ UnitTH python interface """

    @staticmethod
    def run(xml_report_dir, xml_report_filter='TEST-', html_report_path='.', 
        generate_exec_time_graphs=True, html_report_dir='report.th',
        initial_java_heap_size=None, maximum_java_heap_size=None):
        """ Use UnitTH to generate a test history report

        Args:
            xml_report_dir (:obj:`str`): Parent directory of XML reports of individual builds to generate a history report of 
            xml_report_filter (:obj:`str`, optional): Starts-with filter for individual reports with `xml_report_dir` that should 
                be included in the history report. Set `xml_report_filter` to '' to include all files/subdirectories in the history
                report.
            html_report_path (:obj:`str`, optional): Directory of HTML reports of individual builds (relative to XML directories of 
                individual builds)
            generate_exec_time_graphs (:obj:`bool`, optional): Whether execution time graphs shall be generated
            html_report_dir (:obj:`str`, optional): directory to store generated HTML history report
            initial_java_heap_size (:obj:`str`, optional): initial Java heap size
            maximum_java_heap_size (:obj:`str`, optional): maximum Java heap size
        """

        cmd = []
        cmd.append('java')

        if initial_java_heap_size:
            cmd.append('-Xms{}'.format(initial_java_heap_size))
        if maximum_java_heap_size:
            cmd.append('-Xmx{}'.format(maximum_java_heap_size))

        cmd.append('-Dunitth.xml.report.filter={}'.format(xml_report_filter))
        cmd.append('-Dunitth.html.report.path={}'.format(html_report_path))
        cmd.append('-Dunitth.generate.exectimegraphs={}'.format('{}'.format(generate_exec_time_graphs).lower()))
        cmd.append('-Dunitth.report.dir={}'.format(html_report_dir))
        cmd.append('-jar')
        cmd.append('"{}"'.format(resource_filename('unitth', 'lib/unitth/unitth.jar')))
        cmd.append(xml_report_dir)

        subprocess.check_call(' '.join(cmd), shell=True)
