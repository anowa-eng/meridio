from flask import Flask, render_template
from rest.endpoint import Endpoint
from database import models

app = Flask(__name__)
Endpoint.app = app

Endpoint.register(models.User)

@app.route('/')
def index():
    return app.render_template('html/index.html')

if __name__ == '__main__':
    app.run()