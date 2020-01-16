#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pytorch-nyuv2',
    version='1.0',
    description='A Python utility for using the NYUv2 dataset with PyTorch.',
    author='Mihai Suteu',
    maintainer='Anthony Dickson',
    maintainer_email='dican732@student.otago.ac.nz',
    url='https://github.com/eight0153/pytorch-nyuv2',
    packages=['nyuv2'],
    install_requires=['h5py==2.9.0']
)
