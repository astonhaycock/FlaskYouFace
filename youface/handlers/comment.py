import flask
import os
from db import posts, users, helpers

blueprint = flask.Blueprint("comment", __name__)
@blueprint.route('/comment', methods=['POST'])
def comment():
    """Creates a new comment."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    post_id = flask.request.form.get('post_id')
    comment_content = flask.request.form.get('comment')
    posts.add_user_comment(db, user, post_id, comment_content)

    return flask.redirect(flask.url_for('login.index'))