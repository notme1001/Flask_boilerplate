from . import api
from flask import render_template

@api.route('/', methods=['GET'])
def ren_templates():
    return render_template('index.html')