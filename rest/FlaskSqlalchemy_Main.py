from FlaskSqlalchemy_app import db, User, Post, Category

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
# p = Post(title='Snakes', body='Ssssssss')
# py.posts.append(p)
db.session.add(py)
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
