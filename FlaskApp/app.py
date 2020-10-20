import os
from flask import Flask
from __init__ import db, login_manager, bcrypt
from views import view

app = Flask(__name__)

# Routing
app.register_blueprint(view)


# Config
DATABASE_URL = os.environ['DATABASE_URL']

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL+"?sslmode=require"
app.config["SECRET_KEY"] = "A random key to use flask extensions that require encryption"

# Initialize other components
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'view.render_login_page'


bcrypt.init_app(app)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
        port=5000
    )
