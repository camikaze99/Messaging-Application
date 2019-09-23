from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_socketio import SocketIO, send

app = Flask(__name__)
# SINCE AL THE MESSAGES ARE CRYPTED, I USE A KEY
app.config['SECRET_KEY'] = 'oursecret'
# socketio koppelen aan flask
socketio = SocketIO(app)


# listen for the event of a message
@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
	# sent the message aan iedereen die verbonden is met het netwerk
    send(msg, broadcast=True)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


@app.route('/')
@login_required
def home():
    return redirect(url_for("login"))


@app.route('/index')
def index():
    return render_template('./index.html')


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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    # loginpage.run(debug=True)
    # flask runnen in the socket
    socketio.run(app, debug=True)


