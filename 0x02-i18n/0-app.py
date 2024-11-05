#!/usr/bin/env python3
""" simple flask app """
from flask import Flask, render_template
from flask.typing import ResponseReturnValue


app = Flask(__name__)
@app.route('/index')
def home() -> ResponseReturnValue:
    """ returms a simple page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
