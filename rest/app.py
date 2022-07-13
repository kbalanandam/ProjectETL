from model import db, User, Post, Category, app
from flask import request, jsonify
import json
from flask_cors import CORS


# import jwt
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps
CORS(app)


class UnknownException(Exception):

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value


class Posts:
    def __int__(self):
        pass

    @staticmethod
    def get_posts(uid, cid):
        posts = []
        for p in db.session.query(Post).filter(Post.user_id == uid, Post.category_id == cid).all():
            posts.append({"title": p.title, "body": p.body})
        return posts

    @staticmethod
    def add_posts(**post):
        try:

            if db.session.query(User).with_entities(User.id).filter(User.username == post['user']).count() == 0:
                raise UnknownException('unknown user.')
            elif db.session.query(Category).with_entities(Category.id).filter(
                    Category.name == post['category']).count() == 0:
                raise UnknownException('unknown Category.')

            userid = db.session.query(User).with_entities(User.id).filter(User.username == post['user']).one()
            category_id = db.session.query(Category).with_entities(Category.id).filter(
                Category.name == post['category']).one()
            add_post = Post(title=post['title'], body=post['body'], category_id=category_id.id, user_id=userid.id)
            db.session.add(add_post)
            db.session.commit()
            message = 'post created.'

            return jsonify(message)
        except Exception as e:
            return jsonify({'error': str(e)})


class Categories:
    def __int__(self):
        pass

    @staticmethod
    def add_category(cname):
        try:
            category = Category(name=cname)
            db.session.add(category)
            db.session.commit()
            return jsonify('category added.')
        except Exception as e:
            return jsonify({'error': str(e)})

    @staticmethod
    def get_category(cid):
        c = db.session.query(Category).filter(Category.id == cid).one()
        return c.name


class Users:
    def __int__(self):
        pass

    @staticmethod
    def add_users(**user):
        try:
            adduser = User(username=user['name'], email=user['email'])
            db.session.add(adduser)
            db.session.commit()

            return jsonify('user added.')
        except Exception as e:
            return jsonify({'error': str(e)})

    @staticmethod
    def get_users():
        try:
            all_users = []
            users = User.query.all()
            for i in users:
                user = {'name': i.username, 'email': i.email, 'id': i.id}
                all_users.append(user)

            return jsonify({'users': all_users})
        except Exception as e:
            return jsonify({'error': str(e)})

    @staticmethod
    def get_posts(user):
        try:
            user_posts = []
            user_category = []
            category = {}

            user = db.session.query(User).filter(User.username == user).one()
            for c in db.session.query(Post).with_entities(Post.category_id).filter(Post.user_id == user.id).distinct():
                for a in db.session.query(Category).filter(Category.id == c.category_id):
                    category['name'] = Categories.get_category(a.id)
                    category['posts'] = Posts.get_posts(user.id, a.id)
                user_category.append({"name": category['name'], "posts": category['posts']})
            user_posts.append({"user": user.username, "category": user_category})
            return user_posts
        except Exception as e:
            return jsonify({'error': str(e)})


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return Users.get_users()


@app.route('/api/users/add', methods=['POST'])
def api_add_users():
    try:
        user = request.get_json()
        return Users.add_users(**user)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/category/add', methods=['POST'])
def api_add_category():
    try:
        category = request.get_json()
        if category['name']:
            return Categories.add_category(category['name'])
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/posts/add', methods=['POST'])
def api_add_posts():
    try:
        post = request.get_json()
        return Posts.add_posts(**post)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/posts/<username>', methods=['GET'])
def api_get_posts(username):
    try:

        if db.session.query(User).filter(User.username == username).count() == 0:
            raise UnknownException('unknown user.')
        return json.dumps(Users.get_posts(username), indent=4)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
