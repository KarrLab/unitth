from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from unitth.core import UnitTH


class BaseController(CementBaseController):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = "Generate HTML unit test history report"
        arguments = [
            (['xml_report_dir'], dict(type=str,
                                      help='Parent directory of XML reports of individual builds to generate a history report of')),
            (['--xml-report-filter'], dict(type=str, default='TEST-', nargs='?',
                                           help='Starts-with filter for individual reports with `xml-report-dir` that should be included in the history report. Set `xml-report-filter` to '' to include all files/subdirectories in the history report.')),
            (['--html-report-path'], dict(type=str, default='.',
                                          help='Directory of HTML reports of individual builds(relative to XML directories of individual builds)')),
            (['--generate-exec-time-graphs'], dict(type=bool, default=True,
                                                   help='Whether execution time graphs shall be generated')),
            (['--html-report-dir'], dict(type=str, default='report.th',
                                         help='directory to store generated HTML history report')),
            (['--initial_java_heap_size'], dict(type=str, default=None,
                             help='Initial Java heap size')),
            (['--maximum_java_heap_size'], dict(type=str, default=None,
                             help='Maximum Java heap size')),
        ]

    @expose(hide=True)
    def default(self):
        args = self.app.pargs
        UnitTH.run(args.xml_report_dir,
                   xml_report_filter=args.xml_report_filter or '',
                   html_report_path=args.html_report_path,
                   generate_exec_time_graphs=args.generate_exec_time_graphs,
                   html_report_dir=args.html_report_dir, 
                   initial_java_heap_size=args.initial_java_heap_size,
                   maximum_java_heap_size=args.maximum_java_heap_size,
                   )


class App(CementApp):
    """ Command line application """

    class Meta:
        label = 'unitth'
        base_controller = 'base'
        handlers = [BaseController]


def main():
    with App() as app:
        app.run()
