# read the contents of your README file
from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text()

setup(
    name='synthetick',
    version='0.1.0',
    packages=['synthetick'],
    url='https://github.com/mchiuminatto/syntetick.git',
    license='',
    author='mchiuminatto',
    author_email='mchiuminatto@gmail.com',
    description='Library to produce synthetic price time series',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
