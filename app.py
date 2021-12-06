from flask import Flask, request, render_template
from flask_cors import CORS
import os

def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.abspath('.')

    app = Flask(__name__, template_folder=template_dir)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    @app.route('/')
    def landing_page():
        return render_template('index.html')
    @app.route('/services')
    def get_services():
        return render_template('/Services/Services.html')
    @app.route('/learning')
    def get_learning():
        return render_template('/Learning/Learning.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
