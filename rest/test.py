# curl -v http://127.0.0.1:5000/api/users
# curl -d "{\"email\":\"sampath@gmail.com\",\"name\":\"Sampath\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/users/add
# curl -d "{\"title\":\"test oracle post\",\"user\":\"Bala\",\"category\":\"Oracle\",\"body\":\"Oracle learning is always fun!\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/posts/add

from FlaskSqlalchemy_app import db, User, Post, Category, app
from flask import request, jsonify, make_response
import json


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
    def __init__(self, user):
        self.user = user
        self.category = []
        user = db.session.query(User).filter(User.username == self.user).one()

        for value in db.session.query(Post).with_entities(Post.category_id).filter(Post.user_id == user.id).distinct():
            category_id: object = value.category_id
            c = db.session.query(Category).with_entities(Category.name).filter(Category.id == category_id).one()

            self.category.append({"name": c.name, "posts": Posts.get_post(user.id, category_id)})


user1 = Users('admin')
print(json.dumps(user1.__dict__, indent=4))


userid = db.session.query(User).with_entities(User.id).filter(User.username == 'Bala').one()
print(userid)