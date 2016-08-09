from setuptools import setup, find_packages
import unitth
import os

# parse requirements.txt
install_requires = [line.rstrip() for line in open('requirements.txt')]

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
