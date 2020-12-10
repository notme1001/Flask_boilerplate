from flask import Blueprint

api = Blueprint('v1', __name__)

# Import endpoint di sini

from . import routes