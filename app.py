from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'

mail = Mail(app)


    return render_template('abc.html', student=students)

if __name__ == "__main__":
    app.run(debug=True)