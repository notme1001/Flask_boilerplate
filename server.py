#! /usr/bin/env python

import os
from flask_script import Manager
from api import myApp, server

# NAME_APP : your app name
# default : config default in your app
api = myApp(os.getenv('NAME_APP', 'default'))
manager = Manager(api)

@manager.shell
def migration_db():
    return dict(app=api, mongo=server)

if __name__ == '__main__':
    manager.run()