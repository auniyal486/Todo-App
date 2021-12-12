from __init__ import db
from routes import app
with app.app_context():
    db.create_all()