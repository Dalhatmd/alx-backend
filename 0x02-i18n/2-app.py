#!/usr/bin/env python3
""" basic babbel implementation"""
from flask import Flask, render_template, request
from flask_babel import Babel
from flask.typing import ResponseReturnValue
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ class that holds languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config(languages))


@app.route('/')
def home() -> ResponseReturnValue:
    """ returms a simple page """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
