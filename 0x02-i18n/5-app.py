#!/usr/bin/env python3
""" basic babbel implementation"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ class that holds languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)
@babel.localeselector
def get_locale():
    """ gets locale info """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ returms a simple page """
    return render_template('5-index.html')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ sets up global beforr each request """
    g.user = get_user()


def get_user():
    """ logs a user based on id """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
