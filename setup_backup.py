import setuptools
import os.path as path
from pypm.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vintra",
    version=__version__,
    author="Vic",
    author_email="victorda@gmail.com",
    description="Python package manager for projects running Python3.7 and above.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    keywords=['package manager', 'dependency manager', 'manager', 'python 3', 'cli tool', 'command line tool'],
    packages=setuptools.find_packages(),
    package_data={
      'vintra': ['vintra/data/pkg.json', 'vintra/data/pyproject.toml', 'vintra/data/setup.cfg', 'vintra/data/setup.py']
    },
    data_files=[
        ('/vintra/data', [path.join('vintra/data', 'pkg.json')]),
        ('/vintra/data', [path.join('vintra/data', 'pyproject.toml')]),
        ('/vintra/data', [path.join('vintra/data', 'setup.cfg')]),
        ('/vintra/data', [path.join('vintra/data', 'setup.py')])
    ],
    entry_points='''
        [console_scripts]
        vintra=vintra.cli:cli
    ''',
    install_requires=['Click==7.0',  'stdlib-list==0.7.0'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)