#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
     name='Finance',
     version='0.1.0',
     description='Displays your financial information.',
     long_description=('demonstration of how to package a web-app'),
     url='http://github.com/dwwkelly/Finance',
     license='GPLv3',
     author='Devin Kelly',
     author_email='dwwkelly@fastmail.fm',
     packages=find_packages(exclude=['tests*']),
     install_requires=["Flask==0.10.1",
                       "Jinja2==2.7.1",
                       "pymongo==1.0.0",
                       ],
     include_package_data=True,
     entry_points = {
          'console_scripts': [
                 'create_db = Finance.scripts.create_db:main',
                 'load_data = Finance.scripts.load_data:main',
                 'dev_server = Finance.scripts.run_server:dev_server',
                 'run_server = Finance.scripts.run_server:run_server'
               ]
          },
     package_data={
            'static': 'Finance/static/*',
            'templates': 'Finance/templates/*'},
     classifiers=[
            "Private :: Do Not Upload"
          ],
)
