from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product_line')
def product_line():
    return render_template('product_line.html')


@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/sister_companies')
def sister_companies():
    return render_template('sister_companies.html')