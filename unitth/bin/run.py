#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from unitth.core import UnitTH
import argparse


def main():
    """ Command line program to generate a HTML unit test history report """

    parser = argparse.ArgumentParser(description='Generate HTML unit test history report')
    parser.add_argument('xml_report_dir', type=str,
                        help='Parent directory of XML reports of individual builds to generate a history report of')
    parser.add_argument('--xml_report_filter', type=str, default='TEST-', nargs='?',
                        help='Starts-with filter for individual reports with `xml_report_dir` that should be included in the history report. Set `xml_report_filter` to '' to include all files/subdirectories in the history report.')
    parser.add_argument('--html_report_path', type=str, default='.',
                        help='Directory of HTML reports of individual builds(relative to XML directories of individual builds)')
    parser.add_argument('--generate_exec_time_graphs', type=bool, default=True,
                        help='Whether execution time graphs shall be generated')
    parser.add_argument('--html_report_dir', type=str, default='report.th',
                        help='directory to store generated HTML history report')
    args = parser.parse_args()

    UnitTH.run(args.xml_report_dir,
               xml_report_filter=args.xml_report_filter or '',
               html_report_path=args.html_report_path,
               generate_exec_time_graphs=args.generate_exec_time_graphs,
               html_report_dir=args.html_report_dir
               )

if __name__ == "__main__":
    main()
