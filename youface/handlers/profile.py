import flask
from flask import request
from handlers import copy
from db import posts, users, helpers

blueprint = flask.Blueprint("profile", __name__)

@blueprint.route('/profile', methods=['POST'])
def profile():
  username = flask.request.cookies.get('username')
  password = flask.request.cookies.get('password')
  db = helpers.load_db()

  user = users.get_user(db, username, password)
  if not user:
      flask.flash('You need to be logged in to do that.', 'danger')
      return flask.redirect(flask.url_for('login.loginscreen'))
  all_posts = posts.get_posts(db, user)[::-1]

  
  return flask.render_template('profile.html', title=copy.title,
          subtitle=copy.subtitle, posts=all_posts, user=user, username=username, style=users.get_style(db, username, password))

