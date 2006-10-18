from zope import interface

_marker = object()

class ActivationException(Exception):
    """Any exception related to activating or deactivating a feature.
    """

def _set_activation(obj, possibleiface, enhancediface, activation):
    """Try to set the feature activation on the given object.
    """
    
    if isinstance(possibleiface, basestring):
        raise NotImplementedError('Still need to locaate class via dotted '
                                  'path string')
    if isinstance(enhancediface, basestring):
        raise NotImplementedError('Still need to locaate class via '
                                  'dotted path string')

    if not possibleiface.providedBy(obj):
        raise ActivationException('The object denoted by %r does not '
                                  'provide the %r interface' 
                                  % (repr(obj), repr(possibleiface)))

    if not activation and enhancediface.implementedBy(obj.__class__):
        raise ActivationException('It is not possible to remove %r from '
                                  'the %r since the class is the '
                                  'implementer'
                                  % (repr(possibleiface), repr(obj)))

    if activation and not enhancediface.providedBy(obj):
        interface.alsoProvides(obj, enhancediface)
    elif not activation and enhancediface.directlyProvidedBy(obj):
        ifaces = interface.directlyProvidedBy(obj)
        interface.directlyProvides(obj, ifaces - enhancediface)

def activate(obj, possibleiface, enhancediface):
    _set_activation(obj, possibleiface, enhancediface, True)

def deactivate(obj, possibleiface, enhancediface):
    _set_activation(obj, possibleiface, enhancediface, False)

_marker = object()

class FeatureProperty(object):
    """Allows you to get and set the *feature* on the given object.
    """

    def __init__(self, possibleiface, enhancediface, attrname=None):
        self.__possibleiface = possibleiface
        self.__enhancediface = enhancediface
        self.__attrname = attrname

    def __get__(self, inst, class_):
        if inst is None:
            return self

        obj = inst
        if self.__attrname:
            obj = getattr(inst, self.__attrname)
    
        return self.__enhancediface.providedBy(obj)

    def __set__(self, inst, value):
        obj = inst
        if self.__attrname:
            obj = getattr(inst, self.__attrname)
        
        if value:
            activate(obj, self.__possibleiface, self.__enhancediface)
        else:
            deativate(obj, self.__possibleiface, self.__enhancediface)
