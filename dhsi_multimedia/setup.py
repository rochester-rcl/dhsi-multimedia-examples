# to install locally run python3 setup.py sdist && pip3 install -e .

from distutils.core import setup
from setuptools import find_packages

setup(name='ia_tools',
      version='0.0.1',
      packages=find_packages(exclude=['image', 'video', 'audo'])
      )