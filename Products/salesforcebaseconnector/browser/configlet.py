from beatbox import DEFAULT_SERVER_URL
from zope.component import adapts, getUtility, getMultiAdapter
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.formlib import form

from Acquisition import aq_inner
from plone.protect import CheckAuthenticator
from plone.app.form.validators import null_validator

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.controlpanel.form import ControlPanelForm

from Products.salesforcebaseconnector.interfaces.salesforcebaseconnector import IPloneConfiguration
from Products.salesforcebaseconnector import sbcMessageFactory as _


class SalesforceControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IPloneConfiguration)
    
    def __init__(self, context):
        super(SalesforceControlPanelAdapter, self).__init__(context)
        self.context = getToolByName(context, 'portal_salesforcebaseconnector')
    
    def get_username(self):
        return self.context.getUsername()
    
    def set_username(self, value):
        self.context._username = value
    
    username = property(get_username, set_username)
    
    def get_password(self):
        return self.context.getPassword()
    
    def set_password(self, value):
        self.context._password = value
    
    password = property(get_password, set_password)
    
    def get_server_url(self):
        if self.context.serverUrl:
            return self.context.serverUrl
        return DEFAULT_SERVER_URL
    
    def set_server_url(self, value):
        self.context.serverUrl = value
    
    server_url = property(get_server_url, set_server_url)       


class SalesforceControlPanel(ControlPanelForm):
    form_fields = FormFields(IPloneConfiguration)  
    label = _(u"Salesforce configuration")
    description = _(u'Configlet for configuring your connection to \
                        Salesforce.com. Credentials will be tested \
                        and only stored if they can be authenticated.')
    form_name = _(u'Salesforce configuration')
    
    @form.action(_(u'label_save', default=u'Test/store credentials'), 
                        name=u'save')
    def handle_edit_action(self, action, data):
        CheckAuthenticator(self.request)
        sbc = getToolByName(self.context, 'portal_salesforcebaseconnector')
        try:
            sbc.setCredentials(data['username'], 
                               data['password'], 
                               data['server_url'])
        except Exception, exc:
            error = u'The supplied credentials could not be authenticated.  \
                            Salesforce exception code: %s' % exc.faultString
            self.status = _(error)
            return
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _('Authentication tested successfully. \
                                Username and password saved.')
            self._on_save(data)
    
    @form.action(_(u'label_cancel', default=u'Cancel'),
                 validator=null_validator,
                 name=u'cancel')
    def handle_cancel_action(self, action, data):
        IStatusMessage(self.request).addStatusMessage(_("Changes canceled."),
                                                      type="info")
        url = getMultiAdapter((self.context, self.request),
                              name='absolute_url')()
        self.request.response.redirect(url + '/plone_control_panel')
        return ''
    

