
import unittest
import warnings

from zope.component.testing import PlacelessSetup
from zope.configuration import xmlconfig

import zope.app.zcmlfiles


class TestIncludes(PlacelessSetup, unittest.TestCase):

    def _execute(self, filename='configure.zcml',
                 package=zope.app.zcmlfiles, context=None):

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return xmlconfig.file(filename, package, context=context)

    def test_configure(self):
        self._execute('configure.zcml')

    def test_ftesting(self):
        self._execute('ftesting.zcml')

    def test_meta(self):
        self._execute('meta.zcml')

    def test_menus(self):
        context = self._execute('meta.zcml')
        self._execute('menus.zcml', context=context)

    def test_browser(self):
        context = self._execute('meta.zcml')
        context = self._execute('menus.zcml', context=context)
        from zope import security
        context = self._execute(package=security,
                                context=context)
        from zope.app import rotterdam
        context = self._execute(package=rotterdam,
                                context=context)
        from zope import dublincore
        context = self._execute(package=dublincore,
                                context=context)
        self._execute('browser.zcml', context=context)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
