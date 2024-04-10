from flask import Flask
from flask_cors import CORS
from apps.object_detection import object_detection

app = Flask(__name__)
CORS(app)

app.register_blueprint(object_detection, url_prefix='/')

address = '0.0.0.0'
port = 5555

if __name__ == '__main__':
    app.run(debug=True, host=address, port=port)