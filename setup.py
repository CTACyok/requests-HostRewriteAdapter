#!/usr/bin/env python

"""
Simple adapter for requests library to replace host of a request
"""
from setuptools import setup


URL = "https://github.com/CTACyok/requests-HostRewriteAdapter"


if __name__ == "__main__":
    setup(
        name="host-rewrite-adapter",
        version="1.0.0",
        description="Simple adapter for requests library to replace host of a request",
        author="CTAC'yok",
        author_email="CTACyok@gmail.com",
        url=URL,
        provides=['adapters'],
        install_requires=['requests'],

        packages=["host_rewrite_adapter"],

        download_url='{0}/archive/master.zip'.format(URL),
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Plugins",
            "Framework :: Requests",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
        ],

        zip_safe=True,
    )
