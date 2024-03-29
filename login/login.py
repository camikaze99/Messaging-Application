from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import os

loginpage = Flask(__name__)

loginpage.secret_key = os.urandom(24)

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@loginpage.route('/')
@login_required
def home():
    return redirect(url_for("login"))

@loginpage.route('/index')
@login_required
def index():
    return render_template('index.html')

@loginpage.route('/register')
def register():
    return render_template('register.html')

@loginpage.route('/termsandprivacy')
def termsandprivacy():
    return render_template('termsandprivacy.html')

@loginpage.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    usernames=['admin','bob','kees','nick','james']
    passwords=['admin10','bob10','kees10','nick10','james10']

    if request.method == 'POST':
        if request.form['username'] in usernames and request.form['password'] in passwords:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)

@loginpage.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    loginpage.run(debug=True)
