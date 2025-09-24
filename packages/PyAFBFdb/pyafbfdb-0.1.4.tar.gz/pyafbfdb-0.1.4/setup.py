import os
import re
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    open('afbfdb/__init__.py').read()).group(1)

setup(
    # name of the package
    name='PyAFBFdb',
    # You can specify all the packages manually or use the find_package
    # function
    packages=find_packages(),
    # See PEP440 for defining a proper version number
    version=__version__,
    # Small description of the package
    description='Generation of texture database from the package PyAFBF',
    # Long description
    long_description=(read('README.rst') + '\n\n' +
                      read('AUTHORS.rst') + '\n\n'),
    # Project home page:
    url='https://github.com/fjprichard/PyAFBFdb/',
    # license, author and author email
    license='GPLv3',
    author='Frédéric Richard',
    author_email='frederic.richard@univ-amu.fr',
    # If any packages contains data which are not python files, include them
    # package_data={'myapp': 'data'},
    install_requires=['PyAFBF>=0.2.3', 'matplotlib>=3.3.2',
                      'scipy>=1.5.2', 'imageio>=2.9.0'],
    # classifiers is needed for uploading package on pypi.
    # The list of classifiers elements can be found at :
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Image Processing',
    ],
    project_urls={
        'Documentation': 'https://fjprichard.github.io/PyAFBFdb/',
        'Source': 'https://github.com/fjprichard/PyAFBFdb/',
        'Tracker': 'https://github.com/fjprichard/PyAFBFdb/issues',
    },
    # What does your project relate to?
    keywords={'image texture',
              'anisotropic fractional Brownian field',
              'simulation', 'database'},
    # Platforms on which the package can be installed:
    platforms='Linux, MacOSX, Windows',
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'afbfdb=afbfdb',
        ],
    },
)

