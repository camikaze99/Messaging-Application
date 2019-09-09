from flask import Flask, render_template, redirect, url_for, request, session,flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "Welkom01!"

def login_required(f):
    @wraps(f)
    def wrap(args,kwargs):
        if 'logged_in' in session:
            return f(args,kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/termsandprivacy')
def termsandprivacy():
    return render_template('termsandprivacy.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] !='admin':
            error = 'Invalid credentials. Please Try Again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)
