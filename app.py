from flask import Flask, request, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
import os

def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.abspath('.')

    app = Flask(__name__, template_folder=template_dir)
    mail = Mail(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    app.config['MAIL_SERVER'] = 'smtp@gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'johnaziz269@gmail.com'
    app.config['MAIL_PASSWORD'] = "I love my life, i don't want to die."
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(app)

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
    @app.route('/resume')
    def get_resume():
        return render_template('/Resume/Resume.html')

    @app.route('/send-message')
    def send_message():
        msg = Message('Hello', sender="johnaziz269@gmail.com", recipients=['johnaziz269@gmail.com'])
        msg.body = "Hello Flask Message Mail."
        mail.send(msg)
        return "SENT"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
