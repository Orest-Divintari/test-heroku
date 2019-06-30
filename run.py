# we had from db import db inside the __name__ == "main"
# but in the case where uwsgi calls the app.py, the __name__ == "main" is not ran
# so we create another file which runs the app.py
# then we go to uwsgi.ini and we set in the app variable the run.py instead of app.py
from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()