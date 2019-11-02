from app import db


class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    picture_url = db.Column(db.String(1000))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture_url': self.picture_url,
        }
