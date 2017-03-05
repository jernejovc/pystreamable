import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pystreamable",
    version="0.1.0",
    author="Matej Repinc",
    author_email="mrepinc@gmail.com",
    description="streamable.com API wrapper",
    license="MIT",
    keywords="streamable streamable.com api wrapper",
    url="https://github.com/jernejovc/pystreamable",
    packages=['pystreamable'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
