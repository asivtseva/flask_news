from datetime import datetime

from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    news = db.relationship('News', backref='category')

    def __repr__(self):
        return f'Category({self.id}, {self.title})'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return f'News({self.id}, {self.title})'
