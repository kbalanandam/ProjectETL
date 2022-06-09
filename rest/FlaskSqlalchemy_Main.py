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

# Post(title='Oracle!', body='Oracle is the best RDBMS', category=py, user=Bala)


userid = db.session.query(User).with_entities(User.id).filter(User.username == 'Bala').one()
print(userid[0])
categoryid = db.session.query(Category).with_entities(Category.id).filter(Category.name == 'Python').one()
print(categoryid[0])
add_post = Post(title='Hello Python, how are you ?', body='python is the best', category_id=categoryid[0],
                user_id=userid[0])
db.session.add(add_post)
db.session.commit()

all_users = []
users = User.query.all()

Json_text = {
    "user": "Bala",
    "Category": [{
        "category": "Python",
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
