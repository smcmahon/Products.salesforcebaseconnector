from base import SalesforceBaseConnectorTestCase
from Products.CMFCore.utils import getToolByName


class TestInstallation(SalesforceBaseConnectorTestCase):
    def afterSetUp(self):
        """docstring for afterSetUp"""
        self.portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.portal_controlpanel  = getToolByName(self.portal, 'portal_controlpanel')
    
    def testToolInstantiatedOnInstall(self):
        self.assertRaises(AttributeError, getToolByName, self.portal, "portal_salesforcebaseconnector")
        self.portal_quickinstaller.installProduct('Products.salesforcebaseconnector')
        self.failUnless(getToolByName(self.portal, "portal_salesforcebaseconnector"))
    
    def testDefaultConfig(self):
        self.portal_quickinstaller.installProduct('Products.salesforcebaseconnector')
        sbc = getToolByName(self.portal, 'portal_salesforcebaseconnector')
        self.assertEqual('', sbc.getUsername())
        self.assertEqual('', sbc.getPassword())
        self.assertEqual(None, sbc.serverUrl)
        
    def testControlPanelAvailable(self):
        self.portal_quickinstaller.installProduct('Products.salesforcebaseconnector')
        configlets = [config.id for config in self.portal_controlpanel.listActions()]
        self.failUnless('saleforcebaseconnector_config' in configlets)
    
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstallation))
    return suite