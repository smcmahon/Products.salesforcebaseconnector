"""Base class for integration tests, based on ZopeTestCase and CMFTestCase.

Note that importing this module has various side-effects: it registers a set of
products with Zope, and it sets up a sandbox Plone Site site with the appropriate
products installed.
"""
from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

ztc.installProduct('salesforcebaseconnector')
ptc.setupPloneSite()


class SalesforceBaseConnectorTestCase(ptc.PloneTestCase):
    """Base class for Plone integration tests for the 'salesforcebaseconnector' product.
    """