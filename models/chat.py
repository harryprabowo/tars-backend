import datetime
from app import db


class Chat(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    from_user = db.Column(db.Boolean)
    message = db.Column(db.String(1000), nullable=True)
    img_url = db.Column(db.String(1000), nullable=True)
    link = db.Column(db.String(1000), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'date_time': self.date_time,
            'from_user': self.from_user,
            'message': self.message,
            'img_url': self.img_url,
            'link': self.link,
        }
