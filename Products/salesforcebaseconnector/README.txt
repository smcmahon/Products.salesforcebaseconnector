Salesforce Base Connector

 Product home is
 "http://plone.org/products/salesforcebaseconnector":http://plone.org/products/salesforcebaseconnector.
 A "documentation area":http://plone.org/documentation/manual/integrating-plone-with-salesforce.com and "issue
 tracker":http://plone.org/products/salesforcebaseconnector/issues are available at
 the linked locations.

 A Google Group, called "Plone Salesforce Integration":http://groups.google.com/group/plonesf 
 exists with the sole aim of discussing and developing tools to make Plone integrate well
 with Salesforce.com.  If you have a question, joining this group and posting to the 
 mailing list is the likely best way to get support.

 Failing that, please try using the Plone users' mailing list or the #plone irc channel for
 support requests. If you are unable to get your questions answered there, or are 
 interested in helping develop the product, see the credits below for 
 individuals you might contact.

Overview

 The salesforceconnector product provides a Zope-aware tool for 
 interacting with the Python-based beatbox Salesforce client and 
 for storing username and password information for connecting to
 a Salesforce.com instance.

Rationale For This Product

  Salesforce.com provides an extensible, powerful platform from which
  to do Customer Relationship Management (CRM) tasks ranging from sales,
  marketing, nonprofit constituent organizing, and customer service. 
  
  Beatbox is a Python wrapper to the Salesforce.com API (version 7.0), and provides the 
  underpinnings for this product, but suffers from several limitations from within the 
  Zope/Plone integrator space.  
  
  Salesforce Base Connector aims to augment Beatbox for Zope/Plone developers, providing a convenient
  and cleanly integrated set of features:
    * Managing Salesforce credentials
    * Managing http connections to Salesforce
    * Managing Zope permissions over view and edit actions against Salesforce
    * Providing an interface to the Salesforce API from within protected python, for example, 
      in Python Script objects and Zope Page Templates
  
  Additionally, Salesforce Base Connector is intended to decouple Zope/Plone development projects from the specific 
  Python toolkit used as the interface to Salesforce. If a more current alternative to Beatbox
  comes onto the scene, Salesforce Base Connector can be updated to use this code base as its underlying framework.
  
  Salesforce Base Connector is intended to be used as the foundational piece for your own 
  Plone/Salesforce applications. 

Dependencies

  Depends upon the beatbox library, which is a Python wrapper to the
  Salesforce.com API (version 7.0).

  To download and install beatbox, please visit:
    http://code.google.com/p/salesforce-beatbox/

Installation

 Typical for a Zope/Plone product:

  * Install dependencies (see beatbox/README.txt for install instructions)
 
  * Unpack the salesforcebaseconnector product package into the Products folder of the
  Zope/Plone instance. Check your ownership and permissions.

  * Restart Zope.

  * In ZMI, add Salesforce Base Connector to root of site, then set username and password. 
  The credentials will be tested for validity before being stored.

Known Problems

  See TODO.txt 

Credits

  Jesse Snyder and NPower Seattle for the foundation of code that has become
  salesforcebaseconnector

  The Plone & Salesforce crew in Seattle and Portland:

      Jon Baldivieso <jonb@onenw.org>
      Andrew Burkhalter <andrewb@onenw.org>
      Brian Gershon <briang@ragingweb.com>
      Jesse Snyder <jesses@npowerseattle.org>

  Salesforce.com Foundation and Enfold Systems for their gift and work on beatbox (see: 
  http://gokubi.com/archives/onenorthwest-gets-grant-from-salesforcecom-to-integrate-with-plone)

  See the CHANGES.txt file for the growing list of people who helped
  with particular features or bugs.

License

  Distributed under the GPL.

  See LICENSE.txt and LICENSE.GPL for details.

Running Tests

 To run tests in a unix-like environment, do the following:

  cd $INSTANCE/Products/salesforcebaseconnector/tests
  cp sfconfig.py.in sfconfig.py 

    (note: this is done to activate your copy of sfconfig and avoid unintentional 
    checkins of a developer's Salesforce login) 

  edit sfconfig.py with your Salesforce.com USERNAME and PASSWORD
  $INSTANCE/bin/zopectl test -s Products.salesforcebaseconnector
 
 
 FAQ about running tests:
 
    1) If you see an error message like the following and you're certain your 
    login/password combination *IS* valid:
    
      SoapFaultError: 'INVALID_LOGIN' 'INVALID_LOGIN: Invalid username or
      password or locked out.'
 
    You're likely running into one of several security measures in effect at Salesforce.com.
    You can either:
    
      a) Setup your security token within your Salesforce instance and append it to your password
      by following the instructions at:
 
        Setup --> My Personal information --> Reset My Security Token 
        --> edit sfconfig.py to have "mypassword[token]" (where [token] is your security token)
 
      b) Whitelist your IP address at:
      
        Setup --> Security Controls --> Network Access
        
    
    The latter option may be preferable in a production environment, since the security token 
    is more likely to change over time.  For testing, either is fine.
    
    You can find the needed background at:
    http://www.salesforce.com/security/

  2) Often tests can fail if one has aborted the running of the tests midstream, thus bypassing
  the cleanup (i.e. removing fake contacts) that happens after each individual test is run.  If you
  encounter incorrect assertions about the numbers of contacts in your Salesforce instance, 
  try searching for and cleaning up dummy John and Jane Doe contacts.
  
