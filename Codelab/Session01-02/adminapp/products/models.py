from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(500), nullable=True)