#!/usr/bin/env python
import os

from app import create_app

environment = os.getenv('FLASK_CONFIG', 'development')
app = create_app(environment)


if __name__=='__main__':
    app.run()


