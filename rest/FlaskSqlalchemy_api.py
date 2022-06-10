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
        posts = []
        category = []
        json_result = []
        name = username
        if db.session.query(User).filter(User.username == name).count() == 0:
            raise UnknownException('unknown user.')
        user = db.session.query(User).filter(User.username == name).one()
        for p in db.session.query(Post).filter(Post.user_id == user.id).all():
            post = {"title": p.title, "body": p.body}
            posts.append(post)
            for c in db.session.query(Category).filter(Category.id == p.category_id).all():
                cs = {"name": c.name, "posts": posts}
                category.append(cs)
        json_result.append({"user": user.username, "category": category})
        return json.dumps(json_result)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
