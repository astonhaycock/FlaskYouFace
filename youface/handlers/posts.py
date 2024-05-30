import flask
import os
from werkzeug.utils import secure_filename
from db import posts, users, helpers

blueprint = flask.Blueprint("posts", __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@blueprint.route('/post', methods=['POST'])

def post():
    """Creates a new post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))


    post_content = flask.request.form.get('post')

    if 'file' in flask.request.files:
        file = flask.request.files['file']
        if file and allowed_file(file.filename):
            if file.filename:
                filename = secure_filename(file.filename)
                relative_folder = 'static/images'
                os.makedirs(relative_folder, exist_ok=True)
                file_path = os.path.join(relative_folder, filename)
                file.save(file_path)
                posts.add_post(db, user, post_content, file_path=file_path if 'file_path' in locals() else None)
        elif not file and post_content:
            posts.add_post(db, user, post_content, None)
        else:
                flask.flash('No selected file or invalid file name.', 'warning')

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/delete', methods=['POST'])
def delete_post():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    id = flask.request.form.get('post-id')

    posts.delete_user_posts(db, id)


    return flask.redirect(flask.url_for('login.index'))