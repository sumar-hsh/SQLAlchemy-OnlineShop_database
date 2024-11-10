from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    adress = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    orders = db.relationship('Order', backref='customer')

order_products = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable= False, default= datetime.utcnow())
    shipped_date = db.Column(db.DateTime)
    delived_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))
    costumer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    prodects = db.relationship('Product', secondary= order_products)

class Product(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()