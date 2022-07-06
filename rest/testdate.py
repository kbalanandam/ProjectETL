# only run this, if needed some test data set up. otherwise not needed.
from model import db, User, Post, Category


def main():
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    bala = User(username='bala', email='bala@example.com')

    db.session.add(admin)
    db.session.add(guest)
    db.session.add(bala)
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


if __name__ == '__main__':
    main()
