from flask import Blueprint

speech_to_text = Blueprint("speech_to_text", __name__)

from . import routes