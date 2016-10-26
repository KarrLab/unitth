from setuptools import setup, find_packages
import os
import re
import unitth

# parse dependencies and their links from requirements.txt files
install_requires = []
tests_require = []
dependency_links = []

for line in open('requirements.txt'):
    pkg_src = line.rstrip()
    match = re.match('^.+#egg=(.*?)$', pkg_src)
    if match:
        pkg_id = match.group(1)
        dependency_links.append(pkg_src)
    else:
        pkg_id = pkg_src
    install_requires.append(pkg_id)

for line in open('tests/requirements.txt'):
    pkg_src = line.rstrip()
    match = re.match('^.+#egg=(.*?)$', pkg_src)
    if match:
        pkg_id = match.group(1)
        dependency_links.append(pkg_src)
    else:
        pkg_id = pkg_src
    tests_require.append(pkg_id)
dependency_links = list(set(dependency_links))

# install package
setup(
    name="unitth",
    version=unitth.__version__,
    description="Python interface for UnitTH unit test history report generator",
    url="https://github.com/KarrLab/unitth",
    download_url='https://github.com/KarrLab/unitth/tarball/{}'.format(unitth.__version__),
    author="Jonathan Karr",
    author_email="jonrkarr@gmail.com",
    license="MIT",
    keywords='unit test xunit junit unitth HTML history',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={
        'unitth': ['lib/unitth/unitth.jar'],
    },
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'unitth = unitth.__main__:main',
        ],
    },
)
