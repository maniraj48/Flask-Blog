from flaskblog import app, db, User

with app.app_context():
    user_1 = User(username="deva",email="deva@gmail.com",password="salaar")
    user_2 = User(username="varadha",email="varadha@gmail.com",password="salaar")
    
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()
    print(User.query.all())

print("User added!")