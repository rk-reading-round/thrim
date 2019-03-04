from setuptools import setup, setuptools

setup(
  name="thrim",
  version="0.0.1",
  description="thrim package",
  packages=setuptools.find_packages(),
  scripts=[
    'bin/thrim',
    'bin/debug',
  ],
)