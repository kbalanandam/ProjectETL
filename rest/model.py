from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'user'

    def __init__(self, user, password, email, firstname, lastname, gender, createdby ):

        self.user = user
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.createdby = createdby


    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    gender = db.Column(db.String(1))
    user = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    createddate = db.Column(db.DateTime, default=datetime.utcnow)
    createdby = db.Column(db.String(50))

    def json(self):
        return {'user': self.user, 'firstname': self.firstname, 'lastname': self.lastname, 'gender': self.gender}

    @classmethod
    def find_by_username(cls, user)->"User":
        return cls.query.filter_by(user=user).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return '<User %r>' % self.user


class Post(db.Model):
    __tablename__ = 'post'

    def __init__(self, title, body, createdby, uid, cid):
        self.title = title
        self.body = body
        self.createdby = createdby
        self.user_id = uid
        self.category_id = cid

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    category_id = db.Column(db.Integer,
                            nullable=False)
    user_id = db.Column(db.Integer,
                        nullable=False)
    createddate = db.Column(db.DateTime, default=datetime.utcnow)
    createdby = db.Column(db.String(50))

    @staticmethod
    def find_post(uid, cid):
        posts = []
        for p in db.session.query(Post).filter(Post.user_id == uid, Post.category_id == cid).all():
            posts.append({"title": p.title, "body": p.body})
        return posts

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    __tablename__ = 'category'
    def __init__(self, name, description, createdby ):

        self.name = name
        self.description = description
        self.createdby = createdby

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))
    createddate = db.Column(db.DateTime, default=datetime.utcnow)
    createdby = db.Column(db.String(50))

    def json(self):
        return {'name': self.name, 'description': self.description}

    @classmethod
    def find_by_name(cls, name)->"Category":
        return cls.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Category %r>' % self.name

if __name__ == '__main__':
    db.drop_all()
    db.create_all()