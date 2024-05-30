# std imports
import time

# installed imports
import flask
import timeago
import tinydb
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


# handlers
from handlers import friends, login, posts, setting, profile, comment



app = flask.Flask(__name__)



@app.template_filter('convert_time')
def convert_time(ts):
    """A jinja template helper to convert timestamps to timeago."""
    return timeago.format(ts, time.time())

app.register_blueprint(friends.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(posts.blueprint)
app.register_blueprint(setting.blueprint)
app.register_blueprint(profile.blueprint)
app.register_blueprint(comment.blueprint)

app.secret_key = 'mygroup'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True, host='0.0.0.0', port=5001)