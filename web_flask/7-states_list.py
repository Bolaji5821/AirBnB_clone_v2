#!/usr/bin/python3
"""starts a flask application on port 0.0.0.0:5000
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with list of all states obj in db storage
    """
    states = storage.all('state')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
