
from flask import Flask, render_template, redirect, url_for
from main import app

#----------------------------------------------------------------------------------------------

@app.route('/')
def login():
    return render_template('login.html')
    