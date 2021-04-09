from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from constellations import __version__, _program

setup(name='constellations',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'constellations':['data/*']},
      description='files describing constellations for SARS-CoV-2',
      url='https://github.com/cov-lineages/constellations',
      author='cov-lineages group',
      entry_points="""
      [console_scripts]
      {program} = constellations.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)