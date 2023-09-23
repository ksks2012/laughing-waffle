#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup  # pylint: disable=import-error
from setuptools import find_packages

setup(name="umauto",
		version="0.1.0",
		description="An simple program for UMA auto training",
		packages=find_packages(),
		install_requires=[
            "PyAutoGUI >= 0.9.54",
            "opencv-python >= 4.8.0.76"
		],
		entry_points={
				'console_scripts': [
						'uma-auto = umauto.cmd.main:main',
				],
		},
		classifiers=[
				"Development Status :: 3 - Alpha",
				"Intended Audience :: Developers",
				"Operating System :: POSIX",
				"Programming Language :: Python :: 3.10.6",
		],
		)

# vim: tabstop=4 shiftwidth=4
