#!/usr/bin/env python

from flask import render_template, Flask

if __name__ == "__main__":
   FinanceApp = Flask('Finance',
                      static_folder='static',
                      static_url_path='',
                      template_folder='templates')
else:
   from Finance import FinanceApp


@FinanceApp.route('/')
def home():
   return render_template('home.html')


@FinanceApp.route('/about')
def about():
   return render_template('about.html')

if __name__ == "__main__":
   FinanceApp.run(debug=True)
