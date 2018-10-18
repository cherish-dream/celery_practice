#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import create_app
import os


application = create_app(os.getenv('FLASK_CONFIG') or 'default')
application.app_context().push()

if __name__ == '__main__':

    application.run()

