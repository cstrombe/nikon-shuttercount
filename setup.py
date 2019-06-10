# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="nikon-shuttercount",
    version="0.0.1",
    author="Chris Stromberger",
    author_email="chris.stromberger@gmail.com",
    scripts=["shuttercount"],
    url="https://github.com/cstrombe/nikon-shuttercount",
    keywords="exif image metadata nikon shuttercount",
    long_description=open("README.md", "rt").read(),
    install_requires=['ExifRead']
)
