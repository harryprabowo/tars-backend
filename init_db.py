from api import Car
from api import db

if not os.path.exists('db.sqlite'):
    db.create_all()

car1 = Car(name='toyota_innova', picture_url='/uploads/1.jpg')
car2 = Car(name='toyota_supra', picture_url='/uploads/2.jpg')
db.session.add(car1)
db.session.add(car2)
db.session.commit()
