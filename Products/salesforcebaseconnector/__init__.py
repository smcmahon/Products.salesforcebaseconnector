import sys
from Products.CMFCore import utils as cmf_utils
from Products.CMFCore.permissions import setDefaultRoles

this_module = sys.modules[ __name__ ]
 
product_globals = globals()
 
import salesforcebaseconnector
tools = ( salesforcebaseconnector.SalesforceBaseConnector,
          )

from Products.salesforcebaseconnector.interfaces.salesforcebaseconnector import SalesforceRead, SalesforceWrite
setDefaultRoles(SalesforceRead, ('Manager'))
setDefaultRoles(SalesforceWrite, ('Manager'))

def initialize(context):
    cmf_utils.ToolInit('Salesforce Base Connector',
                    tools = tools,
                    product_name = 'salesforcebaseconnector',
                    icon='www/salesforce.gif'
                    ).initialize( context )
