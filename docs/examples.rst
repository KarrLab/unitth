Examples
========

Command line
------------
.. code-block:: text

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

Python
------
.. code-block:: python

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
