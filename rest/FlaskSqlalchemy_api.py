from FlaskSqlalchemy_app import db, User, Post, Category, app
from flask import request, jsonify, make_response
import json
# import jwt
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps


class UnknownException(Exception):

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value


class Posts:
    def __int__(self, uid, cid):
        self.post = []

    @staticmethod
    def get_post(uid, cid):
        post = []
        for p in db.session.query(Post).filter(Post.user_id == uid, Post.category_id == cid).all():
            post.append({"title": p.title, "body": p.body})
        return post


class Users:
    def __init__(self, user) -> object:
        self.user = user
        self.category = []
        user = db.session.query(User).filter(User.username == self.user).one()

        for value in db.session.query(Post).with_entities(Post.category_id).filter(Post.user_id == user.id).all():
            category_id: object = value.category_id
            c = db.session.query(Category).with_entities(Category.name).filter(Category.id == category_id).one()

            self.category.append({"name": c.name, "posts": Posts.get_post(user.id, category_id)})


@app.route('/api/users', methods=['GET'])
def api_get_users():
    try:
        all_users = []
        users = User.query.all()
        for i in users:
            user = {'name': i.username, 'email': i.email, 'id': i.id}
            all_users.append(user)

        return jsonify({'users': all_users})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/users/add', methods=['POST'])
def api_add_users():
    try:
        user = request.get_json()
        adduser = User(username=user['name'], email=user['email'])
        db.session.add(adduser)
        db.session.commit()

        return jsonify('user added.')
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/posts/add', methods=['POST'])
def api_add_posts():
    try:
        post = request.get_json()
        if db.session.query(User).with_entities(User.id).filter(User.username == post['user']).count() == 0:
            raise UnknownException('unknown user.')
        elif db.session.query(Category).with_entities(Category.id).filter(
                Category.name == post['category']).count() == 0:
            raise UnknownException('unknown Category.')

        userid = db.session.query(User).with_entities(User.id).filter(User.username == post['user']).one()
        category_id = db.session.query(Category).with_entities(Category.id).filter(
            Category.name == post['category']).one()

        add_post = Post(title=post['title'], body=post['body'], category_id=category_id[0], user_id=userid[0])
        db.session.add(add_post)
        db.session.commit()
        message = 'post created.'

        return jsonify(message)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/posts/<username>', methods=['GET'])
def api_get_posts(username):
    try:

        name = username
        if db.session.query(User).filter(User.username == name).count() == 0:
            raise UnknownException('unknown user.')
        user = db.session.query(User).filter(User.username == name).one()
        user1 = Users(user.username)
        return json.dumps(user1.__dict__, indent=4)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
