from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

address = '0.0.0.0'
port = 5555

if __name__ == '__main__':
    app.run(debug=True, host=address, port=port)