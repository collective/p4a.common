from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='p4a.common',
      version=version,
      description="Reusable code-bits for Zope 3 and Plone",
      long_description="""""",
      classifiers=[
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Rocky Burt',
      author_email='rocky@serverzen.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['p4a'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
