import flask
from flask import request
from handlers import copy
from db import posts, users, helpers

blueprint = flask.Blueprint("setting", __name__)

@blueprint.route('/setting', methods=['POST'])
def setting():
  username = flask.request.cookies.get('username')
  password = flask.request.cookies.get('password')
  db = helpers.load_db()

  user = users.get_user(db, username, password)
  if not user:
      flask.flash('You need to be logged in to do that.', 'danger')
      return flask.redirect(flask.url_for('login.loginscreen'))
  return flask.render_template('setting.html', title=copy.title,
          subtitle=copy.subtitle, user=user, username=username, style=users.get_style(db, username, password))

@blueprint.route('/save', methods=['POST'])
def save():
  username = flask.request.cookies.get('username')
  password = flask.request.cookies.get('password')
  db = helpers.load_db()

  user = users.get_user(db, username, password)
  if not user:
      flask.flash('You need to be logged in to do that.', 'danger')
      return flask.redirect(flask.url_for('login.loginscreen'))

  radio_value = request.form.get('radio')
  if radio_value == "on":
    users.update_style(db, username, password, "darkyouface.css")
  if radio_value == "off":
    users.update_style(db, username, password, "youface.css")


  return flask.render_template('setting.html', title=copy.title,
          subtitle=copy.subtitle, user=user, username=username, style=users.get_style(db, username, password))
