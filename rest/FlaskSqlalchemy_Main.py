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
        "category": "RDBMS",
        "posts": [{
            "title": "Oracle",
            "body": "Oracle is good."
        }, {
            "title": "MySQL",
            "body": "MySQL is good."
        }]
    }]

}

json_result =[]
for u in db.session.query(User).all():
    user = {"user": u.username}
    posts = []
    category = []
    for p in db.session.query(Post).filter(Post.user_id == u.id).all():
        post = {"title": p.title, "body": p.body}
        for c in db.session.query(Category).filter(Category.id == p.category_id).all():
            cs = {"name":c.name}
            category.append(cs)
            print("User: {}, Category: {}, title: {}, Post: {} ".format(u.username, c.name, p.title, p.body))
            json_result.append(category)
        print("User: {}, Category: {}".format(u.username, c.name))
        json_result.append(posts)
    print("User: {}".format(u.username))
    json_result.append(user)
print(json.dumps(json_result))

