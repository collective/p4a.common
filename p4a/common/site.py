from zope.app.component.hooks import setSite
from zope.app.component.interfaces import ISite, IPossibleSite
try:
    # BBB for Five < 1.5
    from Products.Five.site.localsite import enableLocalSiteHook
except ImportError:
    enableLocalSiteHook = None


def ensure_site(context):
    """Ensure the given context implements ISite.  The importance of
    this method is that it will ensure the given context is an ISite
    regardless of the Zope version (Zope 2.9 had a really hacked up
    SiteManager mechanism we have to account for).

      >>> from zope.app.component.interfaces import ISite, IPossibleSite
      >>> from OFS.Folder import Folder
      >>> if not IPossibleSite.implementedBy(Folder):
      ...    from zope import interface
      ...    from Products.Five.site.metaconfigure import (FiveSite,
      ...                                                  classSiteHook)
      ...    classSiteHook(Folder, FiveSite)
      ...    interface.classImplements(Folder, IPossibleSite)
      >>> om = Folder('foo')

      >>> ISite.providedBy(om)
      False

      >>> try:
      ...     ensure_site(om)
      ... except TypeError:
      ...     # not supposed to do anything unless enableLocalSiteHook was found
      ...     if enableLocalSiteHook is None:
      ...         True
      True
    """

    if not IPossibleSite.providedBy(context):
        if hasattr(context, 'getPhysicalPath'):
            p = '/'.join(context.getPhysicalPath())
        elif hasattr(context, 'getId'):
            p = context.getId()
        elif hasattr(context, 'id'):
            p = id
        else:
            p = str(context)

        raise TypeError('The object, "%s", is not an IPossibleSite' % p)

    if not ISite.providedBy(context):
        if enableLocalSiteHook is not None:
            enableLocalSiteHook(context)
            setSite(context)
        else:
            raise TypeError('"%s" is not configured as an ISite' %
                            '/'.join(context.getPhysicalPath()))

    if not ISite.providedBy(context):
        raise TypeError('Somehow trying to configure "%s" as an ISite '
                        'has failed' % '/'.join(context.getPhysicalPath()))
