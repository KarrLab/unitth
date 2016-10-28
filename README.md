[![PyPI package](https://img.shields.io/pypi/v/unitth.svg)](https://pypi.python.org/pypi/unitth)
[![Documentation](https://readthedocs.org/projects/unitth/badge/?version=latest)](http://unitth.readthedocs.org)
[![Test results](https://circleci.com/gh/KarrLab/unitth.svg?style=shield)](https://circleci.com/gh/KarrLab/unitth)
[![Test coverage](https://coveralls.io/repos/github/KarrLab/unitth/badge.svg)](https://coveralls.io/github/KarrLab/unitth)
[![Code analysis](https://codeclimate.com/github/KarrLab/unitth/badges/gpa.svg)](https://codeclimate.com/github/KarrLab/unitth)
[![License](https://img.shields.io/github/license/KarrLab/unitth.svg)](LICENSE)

# unitth

This package provides a Python method and command line interface for generating HTML reports of unit test histories. The package is a Python interface for the [UnitTH](http://junitth.sourceforge.net).

## Installation
```
pip install unitth
```

## Usage

### Command line
```
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
```

## Example usage

### Python
```
from nose2unitth.core import Converter as nose2unitth
from junit2htmlreport.parser import Junit as JunitParser
from unitth.core import UnitTH
import os
import subprocess

os.mkdir('reports')
os.mkdir('reports/nose')
os.mkdir('reports/unitth')
os.mkdir('reports/html')

subprocess.check_call(['nosetests', 'tests/test_unitth.py:TestDummy.test_dummy_test',
                       '--with-xunit', '--xunit-file', 'reports/nose/1.xml'])
subprocess.check_call(['nosetests', 'tests/test_unitth.py:TestDummy.test_dummy_test',
                       '--with-xunit', '--xunit-file', 'reports/nose/2.xml'])

nose2unitth.run('reports/nose/1.xml', 'reports/unitth/1')
nose2unitth.run('reports/nose/2.xml', 'reports/unitth/2')

with open('reports/unitth/1/index.html', 'wb') as html_file:
    print >> html_file, JunitParser('reports/nose/1.xml').html()
with open('reports/unitth/2/index.html', 'wb') as html_file:
    print >> html_file, JunitParser('reports/nose/2.xml').html()

UnitTH.run('reports/unitth/*', xml_report_filter='', html_report_dir='reports/html')
```

### Command line
```                        
mkdir reports
mkdir reports/nose
mkdir reports/unitth
mkdir reports/html

nosetests tests/test_unitth.py:TestDummy.test_dummy_test --with-xunit --xunit-file reports/nose/1.xml
nosetests tests/test_unitth.py:TestDummy.test_dummy_test --with-xunit --xunit-file reports/nose/2.xml

nose2unitth reports/nose/1.xml reports/unitth/1
nose2unitth reports/nose/2.xml reports/unitth/2

junit2html reports/nose/1.xml reports/unitth/1/index.html
junit2html reports/nose/2.xml reports/unitth/2/index.html

unitth --xml_report_filter --html_report_dir reports/html "reports/unitth/*"
```

## Documentation

Please see the [API documentation](http://unitth.readthedocs.io).

## License
The build utilities are released under the [MIT license](LICENSE).

## Development team
This package was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.
