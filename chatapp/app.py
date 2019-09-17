from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
#SINCE AL THE MESSAGES ARE CRYPTED, I USE A KEY
app.config['SECRET_KEY'] = 'oursecret'
#socketio koppelen aan flask
socketio = SocketIO(app)

#listen for the event of a message
@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
    #sent the message aan iedereen die verbonden is met het netwerk
	send(msg, broadcast=True)

@app.route( '/' )
def index():
  return render_template('./index.html' )

if __name__ == '__main__':
    #flask runnen in the socket
	socketio.run(app)
