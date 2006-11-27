from zope import interface
from zope.component.interfaces import ISiteManager
from zope.app.component.interfaces import ISite

class MockSite:
    """A simple ISite/ISiteManager combo for testing purposes.
    """
    
    interface.implements(ISite, ISiteManager)

    def __init__(self):
        self.utils = {}

    def getUtility(self, iface):
        return self.utils[iface]

    def queryUtility(self, iface):
        return self.utils.get(iface, None)

    def getSiteManager(self):
        return self

    def registerUtility(self, iface, obj):
        self.utils[iface] = obj
