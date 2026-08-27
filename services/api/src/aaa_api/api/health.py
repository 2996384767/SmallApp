from flask import jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from aaa_api.api import api_v1
from aaa_api.extensions import db


@api_v1.get("/health")
def health():
    return jsonify(status="ok")


@api_v1.get("/health/database")
def database_health():
    try:
        db.session.execute(text("SELECT 1"))
    except SQLAlchemyError:
        return jsonify(database="unavailable", status="error"), 503
    return jsonify(database="connected", status="ok")
