from FlaskSqlalchemy_app import db, User, Post, Category

db.drop_all()
db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

py = Category(name='Python')
Post(title='Hello Python!', body='Python is pretty cool', category=py)
p = Post(title='Snakes', body='Ssssssss')
py.posts.append(p)
db.session.add(py)
db.session.commit()

user=User.query.all()
for i in user:
    print (i.username,i.email)

