from flask import Blueprint

object_detection = Blueprint("object_detection", __name__)

from . import routes