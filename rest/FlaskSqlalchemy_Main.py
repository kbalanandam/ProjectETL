from FlaskSqlalchemy_app import db, User, Post, Category
import json

db.drop_all()
db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
Bala = User(username='Bala', email='bala@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.add(Bala)
db.session.commit()

py = Category(name='Python')
p = Post(title='Hi Python!', body='Python is good', category_id=1, user_id=1)
# py.posts.append(p)
db.session.add(py)
db.session.add(p)
db.session.commit()

py = Category(name='Oracle')
p = Post(title='Hi Oracle!', body='Oracle is good', category_id=2, user_id=1)
# py.posts.append(p)
db.session.add(py)
db.session.add(p)
db.session.commit()


p = Post(title='Hi Oracle!', body='Oracle is good', category_id=2, user_id=2)
# py.posts.append(p)
db.session.add(p)
db.session.commit()

all_users = []
users = User.query.all()

Json_result = {
    "user": "Bala",
    "Category": [{
        "name": "Python",
        "posts": [{
            "title": "api",
            "body": "rest apis are good."
        }, {
            "title": "Python",
            "body": "Python apis are good."
        }]
    }, {
        "name": "RDBMS",
        "posts": [{
            "title": "Oracle",
            "body": "Oracle is good."
        }, {
            "title": "MySQL",
            "body": "MySQL is good."
        }]
    }]

}

json_result = []
category = []
posts = []
cs=[]

user = db.session.query(User).filter(User.username == 'guest').one()
for p in db.session.query(Post).filter(Post.user_id == user.id).all():
    post = {"title": p.title, "body": p.body}
    posts.append(post)
    for c in db.session.query(Category).filter(Category.id == p.category_id).all():
        cs = {"name": c.name, "posts": posts}
        category.append(cs)
json_result.append({"user": user.username, "category": category})


print(json.dumps(json_result,indent=4))
