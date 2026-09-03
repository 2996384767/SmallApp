from pathlib import Path

from flask import Flask, jsonify, render_template
from sqlalchemy import text

from aaa_api.api import api_v1
from aaa_api.config import Config
from aaa_api.extensions import cors, db, migrate


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})
    app.register_blueprint(api_v1)

    @app.get("/")
    def index():
        return jsonify(service="AAA Small App API", health="/api/v1/health")

    @app.get("/test")
    def test_page():
        rows = db.session.execute(
            text(
                """
                SELECT
                    id, demand_no, country, category, product_name,
                    quantity, craft, delivery_days, status
                FROM demand
                ORDER BY id
                LIMIT 30
                """
            )
        ).mappings()
        return render_template("test.html", rows=rows)

    return app
