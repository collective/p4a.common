import unittest
from zope.testing import doctest

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite('p4a.common.formatting'),
        doctest.DocTestSuite('p4a.common.site',
                             optionflags=doctest.ELLIPSIS),
        doctest.DocTestSuite('p4a.common.descriptors',
                             optionflags=doctest.ELLIPSIS),
        ))

if __name__ == "__main__":
    unittest.main(defaultTest='test_suite')
