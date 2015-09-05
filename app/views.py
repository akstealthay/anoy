import json

from app import app
from flask import render_template, request, jsonify
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
    filePath = request.args.get('file_path')
    readResponse = FileIO.readFile(filePath)

    error = readResponse.get('error', None)
    rawContent = readResponse.get('raw', None)

    return jsonify(raw=rawContent, error=error)

@app.route('/add/<profile>/<tag>', methods=['POST'])
def addTag(profile, tag):
    error, response = None, None
    appData = FileIO.loadAppData()

    # assert: `profile` should exist before adding tag to it
    if not appData['profile'].has_key(profile):
        # `profile` does not exist hence error
        error = 'Profile %s does not exist, please create one.' % (profile)
    else:
        # `profile` does exists
        tempSet = set(appData['profile'][profile])
        tempSet.add(tag)
        appData['profile'][profile] = list(tempSet)
        FileIO.dumpAppData(appData)

        response = 'Tag %s added successfully to profile %s' % (tag, profile)

    return jsonify(response=response, error=error)

@app.route('/add/<profile>', methods=['POST'])
def addProfile(profile):
    error, response = None, None
    appData = FileIO.loadAppData()

    # assert: `profile` should not exist before adding tag to it
    if appData['profile'].has_key(profile):
        # `profile` does exist hence error
        error = 'Profile %s does exist' % (profile)
    else:
        appData['profile'][profile] = []
        FileIO.dumpAppData(appData)

        response = 'Profile %s created successfully' % (profile)

    return jsonify(response=response, error=error)

@app.route('/data/<key>', methods=['GET'])
def getAppData(key):
    error, response = None, None
    appData = FileIO.loadAppData()

    response = appData.get(key, None)

    if response == None:
        error = 'Invalid data requested'

    return jsonify(response=response, error=error)

@app.route('/data/profile/<profileName>', methods=['GET'])
def getProfileInfo(profileName):
    error, response = None, None
    appData = FileIO.loadAppData()

    response = appData['profile'].get(profileName, None)

    if response == None:
        error = 'Profile %s does not exist.' % (profileName)

    return jsonify(response=response, error=error)