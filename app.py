'''
    https://www.knowledgefactory.net/2020/12/reactjs-python-mongodb-crud-application.html

'''

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml


app     =   Flask(__name__)
config  =   yaml.load(open('database.yaml'))
client  =   MongoClient(config['uri'])
db      =   client['knowledge_factory']
USERS   =   db['users']

CORS(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/users', methods=['POST, GET'])
def data():

    # POST a data to database
    if request.method == 'POST':
        body    =   request.json
        print(body)
        firstName   =   body['firstName']
        lastName    =   body['lastName']
        emailId     =   body['emailId']

        USERS.insert_one({
            "firstName"   :   firstName,
            "lastName"    :   lastName,
            "emailId"     :   emailId
        })

        return jsonify({
            'status'    :   'Data is posted to MongoDB!',
            'firstName' :   firstName,
            'lastName'  :   lastName,
            'emailId'   :   emailId
        })

    # if request.method == 'GET':
    #     allData     =   USERS.find()
    #     dataJson    =   []
    #     for data in allData:
    #         id          =   data['_id']
    #         firstName   =   data['firstName']
    #         lastName    =   data['lastName']
    #         emailId     =   data['emailId']

    #         dataDict    = {
    #             'id'          :   str(id)
    #             'firstName'   :   firstName,
    #             'lastName'    :   lastName,
    #             'emailId'     :   emailId
    #         }
    #         dataJson.append(dataDict)
    #     print(dataJson)
    #     return dataJson



if __name__ == '__main__':
    app.debug = True
    app.run()
