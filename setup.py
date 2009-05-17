from setuptools import setup, find_packages

version = '1.0.4'

setup(name='p4a.common',
      version=version,
      description="Reusable code-bits for Zope 3 and Plone",
      long_description="""""",
      classifiers=[
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone4artists',
      author='Rocky Burt',
      author_email='rocky@serverzen.com',
      url='http://pypi.python.org/pypi/p4a.common/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['p4a'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
