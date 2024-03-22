#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import User


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            # Authentication successful
            # Here you can set a session variable or token to indicate that the user is logged in
            return redirect(url_for('home'))  # Redirect to home page after successful login
        else:
            # Authentication failed
            return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')

@app.route('/signup')
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Create a new user instance
        new_user = User(email=email, password=password)
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))  # Redirect to login page after signup

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
