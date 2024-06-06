# hash.py
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    user = User(username='ali')
    user.set_password('12345')
    db.session.add(user)
    db.session.commit()
    print(f'User {user.username} added to the database.')
