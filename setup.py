#!/usr/bin/env python
#!C:\Python27\python.exe -u

# Set True to force compile native C-coded extension providing direct access
# to inotify's syscalls. If set to False this extension will only be compiled
# if no inotify interface from ctypes is found.
compile_ext_mod = False  # TODO make this a setuputils option/arg

# import statements
import os
import sys
from distutils.core import Extension
from distutils.util import get_platform
try:
    # First try to load most advanced setuptools setup.
    from setuptools import setup
except:
    # Fall back if setuptools is not installed.
    from distutils.core import setup

platform = get_platform()

# check Python's version
if sys.version_info < (2, 4):
    sys.stderr.write('This module requires at least Python 2.6\n')
    sys.exit(1)

# check linux platform
if not platform.startswith('linux') and not platform.startswith('win'):
    sys.stderr.write("pyinotify is not yet available on %s\n" % platform)
    sys.exit(1)


classif = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Operating System :: POSIX :: Linux :: 2.6.13',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Microsoft :: Windows :: 2000/NT',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Filesystems',
    'Topic :: System :: Monitoring',
    ]


# Select branch
if sys.version_info >= (3, 0):
    package_dir = {'': 'python3'}
else:
    package_dir = {'': 'python2'}


def should_compile_ext_mod():
    try:
        import ctypes
        import ctypes.util
    except:
        return True

    libc_name = None
    try:
        libc_name = ctypes.util.find_library('c')
    except:
        pass  # attempt to load it with None anyway.

    libc = ctypes.CDLL(libc_name)

    # check that libc needed inotify/watcher bindings.
    if not (hasattr(libc, 'inotify_init') and
        hasattr(libc, 'inotify_add_watch') and
        hasattr(libc, 'inotify_rm_watch')
        ) or not (hasattr(libc, 'watcher_start') and
        hasattr(libc, 'watcher_stop') ):
        return True

    return False


ext_mod = []
if compile_ext_mod or should_compile_ext_mod():

    # sources for ext
    ext_src = 'inotify_syscalls' if platform.startswith('linux') else 'watcher._watcher'
    # sources for ext module
    ext_mod_src = ['common/inotify_syscalls.c'] if platform.startswith('linux') else ["common/_watcher.c"]

    # add -fpic if x86_64 arch
    if platform in ["linux-x86_64"]:
        os.environ["CFLAGS"] = "-fpic"

    # use higher warning, define unicode charset
    if not platform.startswith('linux'): 
        ext_comp_args = ["/W4", "/DUNICODE"]

    # dst for ext module
    ext_mod.append( Extension(ext_src, ext_mod_src, extra_compile_args=ext_comp_args) )



setup(
    name='pyinotify',
    version='0.1.0',
    description='Xplatform filesystem monitor hacked from pyinotify and watcher',
    author='Eric Butter',
    author_email='hola@ericbeurre.com',
    license='MIT License',
    platforms=['Linux','Win'],
    classifiers=classif,
    url='http://github.com/egbutter/pyinotify',
    ext_modules=ext_mod,
    py_modules=['pyinotify'],
    package_dir=package_dir,
    long_description=open("README.md").read()
    )
