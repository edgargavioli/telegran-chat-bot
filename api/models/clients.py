from .db import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.BigInteger, nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=True, unique=False)
    name = db.Column(db.String(120), nullable=False, unique=False)
    city = db.Column(db.String(255), nullable=True, unique=False)
    address = db.Column(db.String(255), nullable=True, unique=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Client {self.name}>'