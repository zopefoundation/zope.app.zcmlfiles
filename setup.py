##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.app.zcmlfiles package

$Id$
"""

import os

from setuptools import setup, find_packages, Extension

setup(name='zope.app.zcmlfiles',
      version = '3.4.0b1',
      url='http://svn.zope.org/zope.app.zcmlfiles',
      license='ZPL 2.1',
      description='Zope zcmlfiles',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require=dict(test=['zope.app.testing',
                                ]),
      install_requires=['setuptools',
                        'zope.modulealias',
                        'zope.component',
                        'zope.annotation',
                        'zope.app.dependable',
                        'zope.app.content',
                        'zope.publisher',
                        'zope.app.component',
                        'zope.app.generations',
                        'zope.app.interface',
                        'zope.app.publisher',
                        'zope.app.security',
                        'zope.app.form',
                        'zope.app.locales',
                        'zope.app.zopeappgenerations',
                        'zope.app.principalannotation',
                        'zope.app.basicskin',
                        'zope.app.rotterdam',
                        'zope.app.wsgi',
                        'zope.formlib>=3.4.0a1',
                        'zope.i18n',
                        'zope.app.pagetemplate',
                        'zope.app.schema',
                        'zope.app.container',
                        ],
      include_package_data = True,
      zip_safe = False,
      )
