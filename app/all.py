from flask import Blueprint
import os
from .tasks import make_file
from .config_essentials import sample_text, message
bp = Blueprint("all", __name__)

@bp.route("/")
def index():
    return sample_text

@bp.route("/<string:file_name>/<string:content>")
def makefile(file_name, content):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    make_file.delay(file_path, content)
    return message.format(file_path)
