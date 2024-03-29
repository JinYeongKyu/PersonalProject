from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.mask_detection import MaskDetection

app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(MaskDetection,'/mask')

if __name__ == '__main__':
    app.run(debug=True)