[![PyPI package](https://badge.fury.io/py/unitth.svg)](https://pypi.python.org/pypi/unitth)
[![Documentation](https://readthedocs.org/projects/unitth/badge/?version=latest)](http://unitth.readthedocs.org)
[![Test results](https://circleci.com/gh/KarrLab/unitth.svg?style=shield)](https://circleci.com/gh/KarrLab/unitth)
[![Test coverage](https://coveralls.io/repos/github/KarrLab/unitth/badge.svg)](https://coveralls.io/github/KarrLab/unitth)

# unitth

This package provides a Python method and command line interface for generating HTML reports of unit test histories. The package is a Python interface for the [UnitTH](http://junitth.sourceforge.net).

## Installation
```
pip install unitth
```

## Usage

### Command line
```
usage: unitth [-h] [--xml_report_filter XML_REPORT_FILTER]
              [--html_report_path HTML_REPORT_PATH]
              [--generate_exec_time_graphs GENERATE_EXEC_TIME_GRAPHS]
              [--html_report_dir HTML_REPORT_DIR]
              xml_report_dir

Generate HTML unit test history report

positional arguments:
  xml_report_dir        Parent directory of XML reports of individual builds
                        to generate a history report of

optional arguments:
  -h, --help            show this help message and exit
  --xml_report_filter XML_REPORT_FILTER
                        Starts-with filter for individual reports with
                        `xml_report_dir` that should be included in the
                        history report. Set `xml_report_filter` to to include
                        all files/subdirectories in the history report.
  --html_report_path HTML_REPORT_PATH
                        Directory of HTML reports of individual
                        builds(relative to XML directories of individual
                        builds)
  --generate_exec_time_graphs GENERATE_EXEC_TIME_GRAPHS
                        Whether execution time graphs shall be generated
  --html_report_dir HTML_REPORT_DIR
                        directory to store generated HTML history report
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
The build utilities are released under the [MIT license](LICENSE.txt).

## Development team
This package was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.
