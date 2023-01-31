from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title='Home')

@app.route('/shop')
def shop():
    products = {
    'megatutorial': {
        'name': 'Bag of Granola 14 oz',
        'price': 1400,
    },
    'support': {
        'name': 'Granola Bar 3.5 oz',
        'price': 350,
        'per': 'bar',
        'adjustable_quantity': {
            'enabled': True,
            'minimum': 1,
            'maximum': 10,
        },
    },
}
    return render_template('shop.html', title='Shop', products=products)

