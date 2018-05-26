from db import db
import app from app

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()