from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenido a Datos Amables!'

#if __name__ == '__main__':    app.run()
