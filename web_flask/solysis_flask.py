#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.database.database_db import DBStorage
# from models.database.file_storage import FileStorage
from models.user import User


app = Flask(__name__)


storage = DBStorage()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        # User is already logged in, redirect to home page or dashboard
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            # Authentication successful
            session['user_id'] = user.id # Set a session variable  to indicate that the user is logged in
            session['logged_in'] = True  # Set a flag to indicate that the user is logged in
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home page after successful login
        else:
            # Authentication failed
            flash('Invalid email or password', 'error')
            # return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user_id from the session
    session.pop('logged_in', None)
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session:
        # User is already logged in, redirect to home page or dashboard
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        # Create a new user instance
        new_user = User(email=email, password=password, first_name=first_name, last_name=last_name, username=username)
        # Add the new user to the database
        storage.new(new_user)
        storage.save()
        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login page after signup

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
