from app import db


class History(db.Model):
    __tablename__ = 'histories'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    fuel_level = db.Column(db.Float)
    dtc = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime)
    engine_temp = db.Column(db.Float)
    oil_temp = db.Column(db.Float)
    odometer = db.Column(db.Float)
    
    def serialize(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'lat': self.lat,
            'long': self.long,
            'fuel_level': self.fuel_level,
            'dtc': self.dtc,
            'timestamp' : self.timestamp,
            'engine_temp' : self.engine_temp,
            'oil_temp' : self.oil_temp,
            'odometer' : self.odometer,
        }
