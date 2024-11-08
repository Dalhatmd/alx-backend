#!/usr/bin/env python3
""" basic babbel implementation"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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

    # get locale from url
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # get locale from user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # get locale from header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    # default
    print("default locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ returms a simple page """
    return render_template('7-index.html')


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


@babel.timezoneselector
def get_timezone():
    """ gets users timezone """
    # try to get timezone from url
    time_zone = request.args.get('timezone', None)
    if time_zone:
        try:
            return pytz.timezone(time_zone).zone
        except except pytz.exceptions.UnknownTimeZoneError:
            pass

    # get timezone from user settings
    if g.user:
        try:
            timezone = g.user.get('timezone')
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC if timezone not found
    default = app.config['BABEL_CONFIG_TIMEZONE']
    return default


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
