from flask import Flask
from rest.endpoint import Endpoint
from database import models

app = Flask(__name__)
Endpoint.app = app

Endpoint.register(models.User)

if __name__ == '__main__':
    app.run()