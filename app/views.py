from flask import render_template, redirect, url_for

from . import app, db
from .models import News, Category
from .forms import AddNewsForm


@app.route('/')
def index():
    news = News.query.all()
    categories = Category.query.all()
    return render_template('index.html', news=news, categories=categories)


@app.route('/category/<int:id>')
def news_in_category(id):
    news = News.query.filter_by(category_id=id).all()
    categories = Category.query.all()
    category_name = Category.query.get(id).title
    return render_template('category.html', news=news, category_name=category_name, categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    categories = Category.query.all()
    return render_template(
        'news_detail.html',
        news=news,
        categories=categories
    )


@app.route('/add_news', methods=['POST', 'GET'])
def add_news():
    form = AddNewsForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        news.category_id = form.category.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_news.html', form=form, categories=categories)