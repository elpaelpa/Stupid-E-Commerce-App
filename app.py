import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Defaults to a local SQLite file. To use MySQL instead, set DATABASE_URL, e.g.:
#   $env:DATABASE_URL = "mysql+pymysql://user:password@localhost/ecommerce"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///ecommerce.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def home():
    return "E-Commerce DB is running!"


@app.route("/health")
def health():
    """Checks that the app can reach the database."""
    try:
        db.session.execute(text("SELECT 1"))
        return {"status": "ok", "database": db.engine.url.get_backend_name()}
    except Exception as e:
        return {"status": "error", "detail": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
