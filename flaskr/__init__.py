from flask import Flask, jsonify, request
from .models import setup_db, Plant
#from flask_cors import CORS

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    #CORS(app)
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    """
    @app.route('/plants', methods=['GET', 'POST'])
    def list_plants():
        plants = Plant.query.all()
        formatted_plants = [plants.format() for plant in plants]
        
        return jsonify({
            'success':True,
            'plants':formatted_plants
        })
    
    
        return app