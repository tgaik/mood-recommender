from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

import routes
from models import Book
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)