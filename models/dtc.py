from app import db

class DTC(db.Model):
    __tablename__ = 'dtcs'
    id = db.Column(db.Integer, primary_key=True)
    dtc_number = db.Column(db.String(10))
    dtc_name = db.Column(db.String(100))
    desc = db.Column(db.String(1000), nullable=True)
    system = db.Column(db.String(25), nullable=True)
    severity = db.Column(db.Integer)
    urgency = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id': self.id,
            'dtc_number': self.dtc_number,
            'dtc_name': self.dtc_name,
            'desc': self.desc,
            'system': self.system,
            'severity': self.severity,
            'urgency': self.urgency,
        }