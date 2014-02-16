from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Code taken from pip's setup.py
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()
    version_match = re.search(r"^version = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Get the long description from the relevant file
#with open('DESCRIPTION.rst', encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name="megaannex",
    version=find_version('git-annex-remote-mega'),
    description="Hook program for gitannex to use mega.co.nz as backend",
    url='https://github.com/TobiasTheViking/megaannex',

    # Author details
    author='TobiasTheViking',
    author_email='',

    # Choose your license
    #license='MIT',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for

        # Pick your license as you wish (should match "license" above)

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='git-annex remote mega',
    # Main script
    scripts=[
        'git-annex-remote-mega',
    ],
    # Modules to be distributed
    py_modules=[
        'lib/crypto',
        'lib/errors',
        'lib/mega',
        'lib/CommonFunctions',
        'lib/__init__',
    ],
)
