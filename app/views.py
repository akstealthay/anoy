import json

from app import app
from flask import render_template, request, jsonify

from api import TagCore, AppDataCore
from utils import FileIO

def setToList(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/load', methods=['GET'])
def readfile():
    rawContent = None
    filePath = request.args.get('file_path')
    error, response = FileIO.readFile(filePath)

    if error:
        response = None

    return jsonify(response=response, error=error)

@app.route('/act/<profile>/<tag>', methods=['POST'])
def addTag(tag, profile):
    error, response = None, None
    action = request.form.get('action')
    
    if action == 'add':
        error, response = TagCore.addTag(tag, profile)
    elif action == 'delete':
        error, response = TagCore.removeTag(tag, profile)
    
    if error:
        response = None

    return jsonify(response=response, error=error)

@app.route('/act/<profile>', methods=['POST'])
def addProfile(profile):
    error, response = None, None
    action = request.form.get('action')
    
    if action == 'add':
        error, response = TagCore.addProfile(profile)
    elif action == 'delete':
        error, response = TagCore.removeProfile(profile)

    if error:
        response = None

    return jsonify(response=response, error=error)

@app.route('/data/<key>', methods=['GET'])
def getAppData(key):
    error, response = None, None

    print 'In here'
    response = AppDataCore.getAppDataForKey(key)
    print 'res : ', response
    if response == None:
        error = 'Invalid data requested'

    print response, error
    return jsonify(response=response, error=error)

@app.route('/data/profile/<profileName>', methods=['GET'])
def getProfileInfo(profileName):
    error, response = None, None
    
    appData = AppDataCore.getAppData()
    response = appData['profile'].get(profileName, None)

    if response == None:
        error = 'Profile %s does not exist.' % (profileName)

    return jsonify(response=response, error=error)