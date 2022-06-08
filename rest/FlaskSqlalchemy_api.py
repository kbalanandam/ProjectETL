from FlaskSqlalchemy_app import db, User, Post, Category, app
from flask import request, jsonify, make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps


@app.route('/api/users', methods=['GET'])
def api_get_users():
    all_users = []
    users = User.query.all()
    for i in users:
        user = {'name': i.username, 'email': i.email, 'id': i.id}
        all_users.append(user)

    return jsonify({'users': all_users})


@app.route('/api/users/add', methods=['POST'])
def api_add_users():
    user = request.get_json()
    adduser = User(username=user['name'], email=user['email'])
    db.session.add(adduser)
    db.session.commit()

    return jsonify('user added.')


if __name__ == '__main__':
    app.run()



