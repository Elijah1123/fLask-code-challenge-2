from models import db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from models.user import User
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username='admin')
    user.set_password('admin123')

    g1 = Guest(name='Emma Stone', occupation='Actor')
    g2 = Guest(name='Bill Gates', occupation='Philanthropist')
    
    e1 = Episode(date='2023-06-01', number=1)
    e2 = Episode(date='2023-06-02', number=2)

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)

    db.session.add_all([user, g1, g2, e1, e2, a1, a2])
    db.session.commit()
    print("Database seeded!")
