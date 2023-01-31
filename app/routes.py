from flask import render_template, abort, request, redirect,\
    flash, url_for
from app import app, db
from app.models import User, Item
import stripe
from app.forms import RegistrationForm, AddItemForm


@app.route('/register-user', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            password_hash=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('User added')
        return redirect (url_for('register'))
    return render_template('register.html', title='User Registration', form=form)


@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        item = Item(
            name=form.name.data,
            price=form.price.data,
            adjustable_quantity=True,
            per=form.per.data,
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added')
        return redirect(url_for('add_item'))
    return render_template('add_item.html', title='Add Item', form=form)


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title='Home')

@app.route('/shop')
def shop():
    # Products
    myitems = Item.query.all()

    for item in myitems:
        products = {
            item.id: {
            'name': item.name,
            'price': item.price,
            'per': item.per,
            'adjustable_quantity': {
                'enabled': item.adjustable_quantity,
                'minimum': 1,
                'maximum': item.per}
            }
        }
    return render_template('shop.html', title='Shop', products=products)


@app.route('/order/<product_id>', methods=['POST'])
def order(product_id):
    # Products
    myitems = Item.query.all()

    for item in myitems:
        products = {
            item.id: {
            'name': item.name,
            'price': item.price,
            'per': item.per,
            'adjustable_quantity': {
                'enabled': item.adjustable_quantity,
                'minimum': 1,
                'maximum': item.per}
            }
        }
        
    stripe.api_key = app.config['STRIPE_SECRET_KEY']
    if product_id not in products:
        abort(404)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'product_data': {
                        'name': products[product_id]['name'],
                    },
                    'unit_amount': products[product_id]['price'],
                    'currency': 'usd',
                },
                'quantity': 1,
                'adjustable_quantity': products[product_id].get(
                    'adjustable_quantity',
                    {'enabled': False}
                ),
            },
        ],
        payment_method_types=['card'],
        mode='payment',
        success_url=request.host_url + 'order/success',
        cancel_url=request.host_url + 'order/cancel',
    )
    return redirect(checkout_session.url)


@app.route('/order/success')
def success():
    return render_template('success.html', title='Order Successful')


@app.route('/order/cancel')
def cancel():
    return render_template('cancel.html', title='Order Cancelled')
