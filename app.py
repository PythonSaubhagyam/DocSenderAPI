from codecs import IncrementalDecoder
import imp
from flask import Flask, request, jsonify
from flask_restful import reqparse, Api, Resource
import os 

app = Flask(__name__)
api = Api(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class Index(Resource):
    def get(self):
        return jsonify("Docsender api")

class OCRInfo(Resource):
    def post(self):
        int_get = "Hello World"
        image = request.files.getlist("image")
        target = os.path.join(APP_ROOT, 'images')
        filename = image[0].filename
        destination = "/".join([target, filename])
        image[0].save(destination)
        return jsonify(int_get)
    
api.add_resource(OCRInfo, '/get')
api.add_resource(Index, '/')

if __name__ =="__main__":
    app.run(debug=True)
        