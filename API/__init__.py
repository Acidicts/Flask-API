from flask import Flask
from .Scripts.requests import requests

class API:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(requests)

    def run_app(self):
        self.app.run(debug=True)
