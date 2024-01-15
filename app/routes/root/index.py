from flask import Flask
from app import app

@app.route('/')
@app.route('/home')
def home_page():
    return "Hello, welcome to the home page of my biography"