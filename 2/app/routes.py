from app import app
from flask import render_template

@app.route('/')
@app.route('/index.html')

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
