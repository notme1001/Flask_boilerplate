#! /usr/bin/env python

import os
from flask_script import Manager
from api import myApp, db

# NAME_APP : your app name
# default : config default in your app
api = myApp(os.getenv('NAME_APP', 'default'))
manager = Manager(api)

@manager.shell
def migration_db():
    return dict(app=api, db=db)

if __name__ == '__main__':
    manager.run()