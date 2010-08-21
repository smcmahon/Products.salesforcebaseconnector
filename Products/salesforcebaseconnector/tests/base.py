"""Base class for integration tests, based on ZopeTestCase and PloneTestCase.

Note that importing this module has various side-effects: it registers a set of
products with Zope, and it sets up a sandbox CMFSite site with the appropriate
products installed.
"""

from Products.PloneTestCase import PloneTestCase
from Products.salesforcebaseconnector.tests.layer import SalesforceLayer

PloneTestCase.setupPloneSite()

class SalesforceBaseConnectorTestCase(PloneTestCase.PloneTestCase):
    """Base class for integration tests for the 'salesforcebaseconnector' product.
    """

    layer = SalesforceLayer
    
    def afterSetUp(self):
        self.toolbox = self.portal.portal_salesforcebaseconnector
        self._todelete = list() # keep track of ephemeral test data to delete

    def beforeTearDown(self):
        """clean up SF data"""
        if not hasattr(self, '_todelete'):
            return
        ids = self._todelete
        if ids:
            while len(ids) > 200:
                self.toolbox.delete(ids[:200])
                ids = ids[200:]
            self.toolbox.delete(ids)

