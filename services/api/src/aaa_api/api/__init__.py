from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

from aaa_api.api import health  # noqa: E402, F401
