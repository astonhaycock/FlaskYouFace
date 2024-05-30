import time
import tinydb


def add_post(db, user, text, file_path):
    posts = db.table('posts')
    users = db.table('users')
    User = tinydb.Query()
    Post = tinydb.Query()
    
    users.update({"post_count": int(user['post_count']) + 1}, tinydb.where('username')==user['username'])
    post_count = user['username'] + "#" + str(user['post_count'])
    posts.insert({'user': user['username'], 'file_path': file_path, 'text': text, 'time': time.time(), "post_id": post_count, 'comments': []})

def delete_user_posts(db,id):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.remove(Post.post_id == id)
def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.search(Post.user==user['username'])

def get_post_by_id(db,post_id, user):
    user_posts = get_posts(db,user)
    for post in user_posts:
        if post['post_id'] == post_id:
            return post
def add_user_comment(db, user, post_id, comment):
    posts = db.table('posts')
    Post = tinydb.Query()
    post = posts.get(Post.post_id == post_id)
    if post:
       comments = post.get('comments', [])
       comment_with_username = {'username': user['username'], 'comment': comment}
       comments.append(comment_with_username)
       posts.update({'comments': comments}, Post.post_id == post_id)
