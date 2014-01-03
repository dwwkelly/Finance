#!/usr/bin/env python

from Finance import FinanceApp
import Finance.app


def run_server():
    app = FinanceApp
    app.debug = False
    app.run()


def dev_server():
    app = FinanceApp
    app.debug = True
    app.run()

if __name__ == '__main__':
    dev_server()
