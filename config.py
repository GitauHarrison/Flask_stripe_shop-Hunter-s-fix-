import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Stripe
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
