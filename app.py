from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

password = "uneahzmreaczjkln"

def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.abspath('.')

    app = Flask(__name__, template_folder=template_dir)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'omar.khalil498@gmail.com',
    MAIL_PASSWORD = password,
    ))
     
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

    @app.route('/send-message', methods=['POST'])
    def send_message():
        body = request.get_json()
        name = body.get('name', None)
        email = body.get('email', None)
        message = body.get('message', None)
        subject = 'New Message From '+ email +' Via Your Webstie'
        body = "Hello Omar,\n"\
        "This is "+name+ " from your website.\n\n"\
        "My Email: " +email+'.\n'\
        "My Message: "+ message
        try:
            msg = Message(subject, sender='omar.khalil498@gmail.com', recipients=['omar.khalil498@gmail.com'])
            msg.body = body
            mail.send(msg)
            return jsonify({
            'success': True 
            })
        except:
            return jsonify({
                'success': False 
            })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
