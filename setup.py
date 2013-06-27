#!/usr/bin/env python
# setup script for leastsqbound

from distutils.core import setup

setup(
    name='leastsqbound',
    version='1.0',
    author='Jonathan J. Helmus',
    author_email='jjhelmus@gmail.com',
    py_modules=['leastsqbound'],
    license='BSD',
    url='https://github.com/jjhelmus/leastsqbound-scipy',
    description='Constrained multivariate least-squares optimizer',
    long_description=open('README.txt').read(),
    requires=['numpy', 'scipy'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux'
    ]
)
