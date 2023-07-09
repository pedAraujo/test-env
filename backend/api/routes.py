from . import api_bp


@api_bp.route("/")
def index():
    return "This is an api route"
