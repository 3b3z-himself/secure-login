from flask import Flask, render_template, request, jsonify
from utils.backend import *
import json, os
# from flask_sqlalchemy import SQLAlchemy

# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

with open(os.path.abspath('config.json'), 'r') as file:
    connection_params = json.load(file)

app = Flask(__name__)
# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'jobati_secretKey000'

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False)
#     password = db.COlumn(db.String(80), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        response_data = {
            'username': username,
            'password': password,

        }
        return validate_login(response_data, connection_params)

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        response_data = {
            'username': username,
            'password': password,
            'email': email
        }
        register_account(response_data, connection_params)
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port="5000")