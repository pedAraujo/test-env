from flask import Blueprint

routes_bp = Blueprint("routes_blueprint", __name__)


@routes_bp.route("/")
def index():
    return {"messages": ["Hello, World!"]}
