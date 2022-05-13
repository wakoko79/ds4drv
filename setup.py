#!/usr/bin/env python3

from setuptools import setup

import sys

readme = open("README.rst").read()
history = open("HISTORY.rst").read()

sys.executable = "/usr/bin/python3"

setup(name="ds4drv",
      version="0.5.5",
      description="A Sony DualShock 4 userspace driver for Linux",
      url="https://github.com/chrippa/ds4drv",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="MIT",
      long_description=readme + "\n\n" + history,
      entry_points={
        "console_scripts": [
          "ds4drv=ds4drv.__main__:main"
        ]
      },
      packages=["ds4drv",
                "ds4drv.actions",
                "ds4drv.backends",
                "ds4drv.packages"],
      install_requires=["evdev>=0.3.0", "pyudev>=0.16"],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Games/Entertainment"
      ]
)
