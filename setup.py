from __future__ import print_function
from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from subprocess import check_call
import os
import sys
import platform

here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

from distutils import log
log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

LONG_DESCRIPTION = 'Profiler extension for Jupyter notebook to profile the notebook server itself'

version_ns = {}
with open(os.path.join(here, 'nbprofiler', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = {
    'name': 'nbprofiler',
    'version': version_ns['__version__'],
    'description': 'Exposing ipywidgets (or jupyter-js-widgets) outside the notebook',
    'long_description': LONG_DESCRIPTION,
    'data_files': [('etc/jupyter/jupyter_notebook_config.d', ['nbprofiler.json'])],
    'include_package_data': True,
    'author': 'Maarten A. Breddels',
    'author_email': 'maartenbreddels@gmail.com',
    'url': 'https://github.com/maartenbreddels/nbprofiler',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
}

setup(**setup_args)
