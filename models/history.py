from app import db


class History(db.Model):
    __tablename__ = 'histories'
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    avg_speed = db.Column(db.Float)
    top_speed = db.Column(db.Float)
    

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture_url': self.picture_url,
        }
