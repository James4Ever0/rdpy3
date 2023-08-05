#!/usr/bin/env python

import setuptools
from distutils.core import setup, Extension

setup(name='rdpy3',
      version='1.3.7',
      description='Remote Desktop Protocol in Python3',
      long_description_content_type="text/markdown",
      python_requires=">=3",
      long_description=open("README.md").read(),
      # long_description="""
      # RDPY is a pure Python implementation of the Microsoft RDP (Remote Desktop Protocol) protocol (Client and Server side). RDPY is built over the event driven network engine Twisted.

      # RDPY provide RDP and VNC binaries : RDP Man In The Middle proxy which record session, RDP Honeypot, RDP screenshoter, RDP client, VNC client, VNC screenshoter, RSS Player
      # """,
      author='Sylvain Peyrefitte',
      author_email='citronneur@gmail.com',
      url='https://github.com/james4ever0/rdpy3',
      packages=[
          'rdpy3',
          'rdpy3.core',
          'rdpy3.security',
          'rdpy3.protocol',
          'rdpy3.protocol.rdp',
          'rdpy3.protocol.rdp.pdu',
          'rdpy3.protocol.rdp.nla',
          'rdpy3.protocol.rdp.t125',
          'rdpy3.protocol.rfb',
          'rdpy3.ui'
      ],
      ext_modules=[Extension('rle', ['ext/rle.c'])],
      scripts=[
          'bin/rdpy3-rdpclient.py',
          'bin/rdpy3-rdphoneypot.py',
          'bin/rdpy3-rdpmitm.py',
          'bin/rdpy3-rdpscreenshot.py',
          'bin/rdpy3-rssplayer.py',
          'bin/rdpy3-vncclient.py',
          'bin/rdpy3-vncscreenshot.py'
      ],
      install_requires=[
          'twisted',
          'pyopenssl',
          'service_identity',
          'qt5reactor',
          'rsa',
          'pyasn1'
      ],
      )
