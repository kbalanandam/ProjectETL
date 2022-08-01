from model import db, User, Post, Category, app
from flask import jsonify
from flask_cors import CORS
from flask_restful import reqparse, Api, Resource


# import jwt
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps
CORS(app)
api = Api(app)


class UsersApi(Resource):

    def get(self):
        try:
            all_users = []
            users = User.query.all()
            for i in users:
                user = {'firstname': i.firstname, 'lastname': i.lastname, 'gender': i.gender, 'user': i.user,
                        'email': i.email, 'id': i.id, 'createdon': i.createddate}
                all_users.append(user)

            return jsonify({'users': all_users})
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str, required=True, help='user name cannot be blank')
        parser.add_argument('password', type=str, required=True, help='this cannot be blank')
        parser.add_argument('email', type=str, required=True, help='email cannot be blank')
        parser.add_argument('firstname', type=str, required=True)
        parser.add_argument('lastname', type=str, required=True)
        parser.add_argument('gender', type=str, required=True)
        try:
            _user = parser.parse_args()
            if User.find_by_username(_user['user']):
                return {'messageType': 'Error', 'message': "An user with name '{}' already exists.".format(_user['user'])}, 400
            new = User(user=_user['user'], password=_user['password'], email=_user['email'], firstname=_user['firstname'], lastname=_user['lastname'],
                    gender=_user['gender'], createdby='UsersApi')
            new.save_to_db()
            return {'messageType': 'Success', "message": "user {}, is created successfully.".format(_user['user'])}
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


class UserApi(Resource):

    def get(self, user):
        try:
            _user = User.find_by_username(user)
            if _user:
                return _user.json()
            return {'messageType': 'Error', 'message': 'user not found'}, 404
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 201

    def delete(self, user):
        try:
            _user = User.find_by_username(user)
            if _user:
                _user.delete_from_db()
                return {'messageType': 'Success', "message": "user deleted."}
            return {'messageType': 'Error', 'message': 'user not found'}, 404

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


class CategoriesApi(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Category name cannot be blank')
        parser.add_argument('description', type=str, required=False, help='Description is optional')
        try:

            _category = parser.parse_args()
            if Category.find_by_name(_category['name']):
                return {'messageType': 'Error', 'message': "A category with name '{}' already exists.".format(_category['name'])}, 400

            new = Category(name=_category['name'], description=_category['description'], createdby='CategoriesApi')
            new.save_to_db()
            return {'messageType': 'Success', 'message': "Category {}, is created successfully.".format(_category['name'])}, 201
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


class CategoryApi(Resource):

    def get(self, category):
        try:
            _category = Category.find_by_name(category)
            if _category:
                return _category.json()
            return {'messageType': 'Error', 'message': 'category not found'}, 404

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500

    def delete(self, category):
        try:
            _category = Category.find_by_name(category)
            if _category:
                _category.delete_from_db()
                return {'messageType': 'Success', "message": "category deleted."}
            return {'messageType': 'Error', 'message': 'category not found'}, 404

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


class UserPostApi(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='title cannot be blank')
        parser.add_argument('body', type=str, required=True, help='body cannot be blank')
        parser.add_argument('category', type=str, required=True, help='category cannot be blank')
        parser.add_argument('user', type=str, required=True, help='user cannot be blank')
        try:
            _post = parser.parse_args()

            _category = Category.find_by_name(_post['category'])
            if _category is None:
                return {'messageType': 'Error', 'message': 'category not found'}, 404

            _user = User.find_by_username(_post['user'])
            if _user is None:
                return {'messageType': 'Error', 'message': 'user not found'}, 404

            new = Post(title=_post['title'], body=_post['body'], cid=_category.id, uid=_user.id, createdby='UserPostApi')
            new.save_to_db()

            return {'messageType': 'Success', 'message': 'post created.'}, 201
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


class PostbyUserApi(Resource):

    def get(self, user):
        try:

            user_category = []
            category = {}

            _user = User.find_by_username(user)
            if _user is None:
                return {'messageType': 'Error', 'message': 'user not found'}, 404
            for c in db.session.query(Post).with_entities(Post.category_id).filter(Post.user_id == _user.id).distinct():
                for a in db.session.query(Category).filter(Category.id == c.category_id):
                    category['name'] = a.name
                    category['posts'] = Post.find_post(_user.id, a.id)
                user_category.append({"name": category['name'], "posts": category['posts']})
            return {'user': user, 'category': user_category}
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


api.add_resource(UsersApi, '/api/users', endpoint='users')
api.add_resource(UserApi, '/api/users/<user>', endpoint='user')
api.add_resource(CategoriesApi, '/api/categories', endpoint='categories')
api.add_resource(CategoryApi, '/api/categories/<category>', endpoint='category')
api.add_resource(UserPostApi, '/api/posts', endpoint='creatpost')
api.add_resource(PostbyUserApi, '/api/posts/<user>', endpoint='userposts')


if __name__ == '__main__':
    app.run()
