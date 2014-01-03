#!/usr/bin/env python

# pylint: disable=C
from flask import Flask

FinanceApp = Flask(__name__,
                   static_folder='static',
                   static_url_path='',
                   template_folder='templates')
