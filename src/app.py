from crypt import methods
from flask import Flask
from flask import render_template, redirect, request, flash, session
import db_queries

app = Flask(__name__)
app.secret_key = 'verysecrettoken1'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login-page")
def login():
    return render_template("loginpage.html")

@app.route("/execute-login", methods=["POST"])
def execute_login():
    username = request.form["username"]
    password = request.form["password"]
    result = db_queries.select_username(username)
    if result:
        if password == result[0][2]:
            flash('login successful!')
            session['username'] = result[0][1]
            return redirect('/')
        else:
            flash('login failed check username and password')
            return redirect('/login-page')

    flash('login failed check username and password')
    return redirect('/login-page')

@app.route('/logout')
def logout():
    del session["username"]
    return redirect("/")

@app.route("/create-account-page")
def create_account_page():
    return render_template("create_new_account_page.html")

@app.route('/create-new-account', methods=["POST"])
def create_new_account():
    username = request.form['username']
    password = request.form['password']
    username_taken = db_queries.select_username(username)
    if username_taken:
        flash('Username already taken. Please choose a new one')
        return redirect('/create-account-page')
    else:
        flash('New user created!')
        db_queries.create_new_account(username, password)
        return redirect('/login-page')

@app.route('/view-account/<username>')
def view_account(username):
    account_data = db_queries.select_username(username)
    return render_template('view_account.html', account_data=account_data)

@app.route('/change-password', methods=["POST"])
def change_password():
    username = session['username']
    password1 = request.form['password1']
    password2 = request.form['password2']

    if password1 != password2:
        flash('Passwords did not match')
        return redirect('/')

    db_queries.change_password(username, password1)
    flash('Password changed!')
    return redirect('/')
    