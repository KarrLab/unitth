Command line interface documentation
====================================
.. code-block:: text

  usage: unitth (sub-commands ...) [options ...] {arguments ...}

  Generate HTML unit test history report

  positional arguments:
    xml_report_dir        Parent directory of XML reports of individual builds
                          to generate a history report of

  optional arguments:
    -h, --help            show this help message and exit
    --debug               toggle debug output
    --quiet               suppress all output
    --xml-report-filter [XML_REPORT_FILTER]
                          Starts-with filter for individual reports with `xml-
                          report-dir` that should be included in the history
                          report. Set `xml-report-filter` to to include all
                          files/subdirectories in the history report.
    --html-report-path HTML_REPORT_PATH
                          Directory of HTML reports of individual
                          builds(relative to XML directories of individual
                          builds)
    --generate-exec-time-graphs GENERATE_EXEC_TIME_GRAPHS
                          Whether execution time graphs shall be generated
    --html-report-dir HTML_REPORT_DIR
                          directory to store generated HTML history report
    --initial_java_heap_size INITIAL_JAVA_HEAP_SIZE
                          Initial Java heap size
    --maximum_java_heap_size MAXIMUM_JAVA_HEAP_SIZE
                          Maximum Java heap size
