from api import db

class Brake(db.Model):
    __tablename__ = 'histories'
    id = db.Column(db.Integer, primary_key=True)
    brake_fluid = db.Column(db.String(100))
    avg_speed = db.Column(db.Float)
    top_speed = db.Column(db.Float)
    

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture_url': self.picture_url,
        }