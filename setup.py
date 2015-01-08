from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dgcn.policy',
      version=version,
      description="DGCN Project Policy Package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone',
      author='marr',
      author_email='',
      url='http://github.com/l34marr/dgcn.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dgcn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
