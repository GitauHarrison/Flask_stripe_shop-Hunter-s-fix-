Fixes:

- Restructure project

```python
project_folder
    | --- requirements.txt
    | --- main.py
    | --- config.py
    | --- .env
    | --- .flaskenv
    | --- app/
           | --- __init__.py
           | --- routes.py
           | --- forms.py
           | --- models.py
           | --- errors.py # not done yet
           | --- static/
                   | --- images/
                   | --- css/
                          | --- custom.css
            | --- templates/

```

Run migrations in your root directory:

```python
(venv)flask db init # create migration folder
(venv)flask db migrate -m 'all models' # create migration scripts (versions)
(venv) flask db upgrade # apply the changes
```

Notes:

- All your secret keys should be in `.env` file
- They are accessed from `config.py`
    - how to access a secret key: `app.config['SECRET_KEY']`
- `.flaskenv` is used to store environment variables used by the flask server

Version control:

- Use `.gitignore` to ignore select files. 
- This file lives in the root directory, so create it there
- Check what to ignore [here](https://github.com/github/gitignore) (Python.gitignore)

Reference:

- Check [this repo](https://github.com/GitauHarrison/integrating-stripe-payment-in-flask) for the same project. You may learn another method of using Stripe.

Recommendations:

- Consider reviewing [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Final:

- Consider renaming your branch "main" instead of "master" :-)