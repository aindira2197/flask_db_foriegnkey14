from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)


class Courier(db.Model):
    __tablename__ = 'couriers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    orders = db.relationship('Order', backref='courier', cascade="all, delete")


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)

    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.id', ondelete='CASCADE'))

    packages = db.relationship('Package', backref='order', cascade="all, delete")


class Package(db.Model):
    __tablename__ = 'packages'
    id = db.Column(db.Integer, primary_key=True)

    weight = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='CASCADE'))

    tracking = db.relationship('Tracking', backref='package', cascade="all, delete")


class Tracking(db.Model):
    __tablename__ = 'trackings'
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.String(50))
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


menga shunaqa 100 foiz toliq qilib 5 ta masala yozib ber
