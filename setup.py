# -*- coding:utf-8 -*-
from setuptools import setup
from Twitterlib import __author__, __version__

setup(
        name             = 'Twitterlib',
        version          = __version__,
        author           = __author__,
        packages         = ['Twitterlib'],
        install_requires = ['requests-oauthlib']
)
