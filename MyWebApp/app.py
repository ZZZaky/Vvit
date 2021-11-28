import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database = "serv_db",
                        user = "postgres",
                        password = "2003",
                        host = "localhost",
                        port = "5432")
cursor = conn.cursor()

@app.route('/login/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login = %s AND password = %s", (username, password))
            records = list(cursor.fetchall())
            
            if username and password and records:
                return render_template('account.html', full_name = records[0][1], login = records[0][2], password = records[0][3])
            else:
                return redirect('/login/')
        elif request.form.get('registration'):
            return redirect('/registration/')
    else:
        return render_template('login.html')


@app.route('/registration/', methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        
        if name and login and password:
            cursor.execute("SELECT * FROM service.users WHERE login = %s", (login,))
            records = list(cursor.fetchall())
            
            if not records:
                cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);', (name, login, password))
                return redirect('/login/')
        
        conn.commit()
    else:
        return render_template('registration.html')