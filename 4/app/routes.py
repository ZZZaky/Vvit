from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Yura'}
    posts = [
        {
            'author': {'username': 'Johnny'},
            'body': 'Oh hi Mark'
        },
        {
            'author': {'username': 'Mark'},
            'body': 'Oh hi Johnny'
        },
        {
            'author': {'username': 'Ms. Steffany'},
            'body': 'The program is working like it should'
        }
    ]
    return render_template('index.html', title = 'Welcome to HELL', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title = 'Sign In', form = form)