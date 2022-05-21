'''
    https://www.knowledgefactory.net/2020/12/reactjs-python-mongodb-crud-application.html

'''

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml



