Change History
==============

6.0 (2025-09-12)
----------------

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.1 (2025-08-07)
----------------

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-07-10)
----------------

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


4.1.0 (2022-08-23)
------------------

- Add support for Python 3.7, 3.8, 3.9, 3.10.

- Drop support for Python 3.4.


4.0.0 (2017-05-29)
------------------

- Add support for Python 3.4, 3.5, 3.6 and PyPy. Update minimum dependency
  versions appropriately.


3.8.0 (2013-08-27)
------------------

- Remove include of ``zope.app.zopeappgenerations`` that is not useful unless
  upgrading a database older than Zope 3.4.  This cuts the last dependency on
  ``zope.app.authentication`` from the ZTK.


3.7.1 (2011-07-26)
------------------

- Move include of ``zope.dublincore.browser`` here from ``zope.dublincore``
  (LP: #590668).


3.7.0 (2009-12-28)
------------------

- Use new ``zope.app.locales`` which has its own `configure.zcml`.

- No longer using ``zope.testing.doctestunit`` as it is deprecated
  now. Using python's ``doctest`` module.

3.6.1 (2009-12-16)
------------------

- Removed reference to no longer existing configure.zcml from
  ``zope.app.pagetemplate.tests``.


3.6.0 (2009-07-11)
------------------

- No longer depends on deprecated ``zope.app.interface`` but on
  ``zope.componentvocabulary``.


3.5.5 (2009-05-23)
------------------

- Added missing dependencies, including ``zope.app.http`` and
  ``zope.app.applicationcontrol``.


3.5.4 (2009-05-18)
------------------

- Added missing ``zope.app.exception`` dependency, as we include its ZCML.

- Added missing ``zope.app.testing`` test dependency to make tests pass.


3.5.3 (2009-02-04)
------------------

- Added ``zope.app.broken`` dependency (we include its ZCML).

3.5.2 (2009-01-31)
------------------

- We depended on ``zope.formlib`` but didn't include its configuration. Now
  it's included in ``configure.zcml``.

- We include ZCML of ``zope.app.error`` but didn't mention it as a dependency.

3.5.1 (2008-12-28)
------------------

- Add include of ``zope.app.schema:configure.zcml``. Because component-based
  vocabularies are used everywhere and we need to import zope.app.schema
  somehow to make it work. This is needed because of removal of the include
  of zope.app.schema's meta.zcml in the previous release.

3.5.0 (2008-12-16)
------------------

- Remove deprecated include of ``zope.app.component.browser:meta.zcml``.
- Remove deprecated include of ``zope.app.schema:meta.zcml``.
- Remove use of zope.modulealias.

3.4.3 (2007-11-01)
------------------

- Fix test failure due to missing ``zope.app.container.browser.ftests``
   directory.  Now it is moved to ``zope.app.container.browser.tests``.

3.4.2 (2007-10-30)
------------------

- Fix test failure due to missing ``zope.app.form.browser.ftests`` directory.
  Now it is moved to ``zope.app.form.browser.tests``.

3.4.1 (2007-10-23)
------------------

- Added missing dependency.

3.4.0 (2007-10-03)
------------------

- Initial public release as an individual package.
