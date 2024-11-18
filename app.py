from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambia 'your_secret_key' por una clave secure
socketio = SocketIO(app)

# Ruta para el índice
@app.route('/')
def index():
    return render_template('index.html')

# Evento que maneja los mensajes
@socketio.on('message')
def handleMessage(msg):
    print('Mensaje:', msg)
    send(msg, broadcast=True)  # Envía el mensaje a todos los clients conectados

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render asignará el puerto
    socketio.run(app, host='0.0.0.0', port=port)
