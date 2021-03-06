from flask import Flask, render_template, request
import smtplib
import os

# Configure application
app = Flask(__name__)
app.static_folder = 'static'
# app.template_folder='templates'
# subscribers = []  

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    title = 'Portfolio - Khalid Gharib'
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    title = 'Blog - Khalid Gharib'
    return render_template('blog.html')

@app.route('/about')
def about():
    title = 'About Me'
    return render_template('about.html')

@app.route('/contact')
def contact():
    title = 'Contact Info - Khalid Gharib'
    return render_template('contact.html')

@app.route('/subscribe')
def subscribe():
    title = 'Subscribe - Khalid Gharib'
    return render_template('subscribe.html')

# @app.route('/form', methods=['POST'])
# def form():
#     title = 'Form'
#     first_name= request.form.get("first_name")
#     last_name= request.form.get("last_name")
#     email = request.form.get("email")
#     # message = 'You have subscribed to my Email newsletter'

#     # server = smtplib.SMTP("smtp.gmail.com", 587)
#     # server.starttls()
#     # server.login("khalid.gharib1994@gmail.com", os.getenv("PASSWORD"))
#     # server.sendmail("khalid.gharib1994@gmail.com", email, message)

#     if not first_name or not last_name or not email:
#         error_statement = 'Missing Fields, please try again.'
#         return render_template('subscribe.html', error_statement=error_statement
#                                 ,first_name=first_name
#                                 ,last_name=last_name
#                                 ,email=email)
#     subscribers.append(f'{first_name} {last_name} | {email}')
#     return render_template('form.html',subscribers=subscribers)

