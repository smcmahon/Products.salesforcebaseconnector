import sys
from Products.CMFCore.permissions import AddPortalContent
from Products.CMFCore import utils as cmf_utils
from Products.Archetypes.public import process_types, listTypes

this_module = sys.modules[ __name__ ]
 
product_globals = globals()
 
import salesforcebaseconnector
tools = ( salesforcebaseconnector.SalesforceBaseConnector,
          )

def initialize(context):
    cmf_utils.ToolInit('Salesforce Base Connector',
                    tools = tools,
                    product_name = 'salesforcebaseconnector',
                    icon='www/salesforce.gif' 
                    ).initialize( context )
