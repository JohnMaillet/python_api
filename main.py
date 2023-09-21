# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


def buildMockResponse(type):
    try:
        with open(f'./mock/{type}_mock.json') as file:
            file_contents = file.read()
        parsed_json = json.loads(file_contents)
        code = 200
        return parsed_json, code
    except 'Resource Not Found':
        parsed_json = None
        code = 404
        return parsed_json, code


@app.route("/user")
# methods go here
def getUsers():
    parsed_json = {"userId": "1", "firstName": "Steven", "lastName": "Strange",  "age": "43", "addressInformation": {"streetAddress": "123 Sesame Street", "city": "New York",  "state": "NY"}}
    code = 200
    return jsonify(message=parsed_json, status=code)


@app.route("/location")
def getLocations():
    parsed_json = {"name": "Rixos The Palm Dubai","position": [25.1212, 55.1535], "locationId": "1"}
    code = 200
    return jsonify(message=parsed_json, status=code)


# api.add_resource(Users, '/users')  # '/users' is our entry point
# api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app
