from flask import Flask, jsonify
#from models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    @app.route('/')
    def hello():
        return "Hello World!"
    
    @app.route('/name')
    def name():
        return jsonify({'name': 'Faith'})
    
    
    return app