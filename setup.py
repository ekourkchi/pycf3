#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019, Juan B Cabral
# License: BSD-3-Clause
#   Full Text: https://github.com/quatrope/pycf3/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""This file is for distribute pycf3

"""


# =============================================================================
# IMPORTS
# =============================================================================

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup # noqa


# =============================================================================
# CONSTANTS
# =============================================================================

REQUIREMENTS = ["numpy", "requests", "attrs", "bokeh", "pyquery"]

with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()

DESCRIPTION = LONG_DESCRIPTION.splitlines()[2]


# =============================================================================
# FUNCTIONS
# =============================================================================

def do_setup():
    setup(
        name="pycf3",
        version="2019.9",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author="QuatroPe",
        author_email="jbc.develop@gmail.com",
        url="https://github.com/quatrope/pycf3",
        license="3 Clause BSD",
        keywords=[
            "astronomy", "cosmicflow", "Distance", "Velocity", "calculator"],
        classifiers=(
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering"),
        py_modules=["pycf3", "ez_setup"],
        install_requires=REQUIREMENTS)


if __name__ == "__main__":
    do_setup()