from setuptools import setup

setup(
    name="pystreamable",
    version="1.0.1",
    author="Matej Repinc",
    author_email="mrepinc@gmail.com",
    description="streamable.com API wrapper",
    license="MIT",
    keywords="streamable streamable.com api wrapper",
    url="https://github.com/jernejovc/pystreamable",
    packages=['pystreamable'],
    long_description=("A wrapper for streamable.com API, supports uploading "
                      "videos, importing videos, retrieving videos to and "
                      "from streamable.com."),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
