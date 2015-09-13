import json

from app import app
from flask import render_template, request, jsonify

from api import TagCore, AppDataCore

from utils import FileIO
from utils.logger import logger

def setToList(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

@app.route('/')
@app.route('/index')
def index():
    logger.info('Hitting URL %s', request.url)
    return render_template('index.html')

@app.route('/load', methods=['GET'])
def readfile():
    logger.info('Hitting URL %s', request.url)

    rawContent = None
    filePath = request.args.get('file_path')
    error, response = FileIO.readFile(filePath)

    if error:
        response = None

    logger.debug('Error: %s', error)
    logger.debug('Response: %s', response)
    return jsonify(response=response, error=error)

@app.route('/act/<profile>/<tag>', methods=['POST'])
def addTag(tag, profile):
    logger.info('Hitting URL %s', request.url)

    error, response = None, None
    action = request.form.get('action')
    
    if action == 'add':
        error, response = TagCore.addTag(tag, profile)
    elif action == 'delete':
        error, response = TagCore.removeTag(tag, profile)
    
    if error:
        response = None

    logger.debug('Error: %s', error)
    logger.debug('Response: %s', response)
    return jsonify(response=response, error=error)

@app.route('/act/<profile>', methods=['POST'])
def addProfile(profile):
    logger.info('Hitting URL %s', request.url)

    error, response = None, None
    action = request.form.get('action')
    
    if action == 'add':
        error, response = TagCore.addProfile(profile)
    elif action == 'delete':
        error, response = TagCore.removeProfile(profile)

    if error:
        response = None

    logger.debug('Error: %s', error)
    logger.debug('Response: %s', response)
    return jsonify(response=response, error=error)

@app.route('/data/<key>', methods=['GET'])
def getAppData(key):
    logger.info('Hitting URL %s', request.url)

    error, response = None, None
    response = AppDataCore.getAppDataForKey(key)

    if response == None:
        error = 'Invalid data requested'

    logger.debug('Error: %s', error)
    logger.debug('Response: %s', response)
    return jsonify(response=response, error=error)

@app.route('/data/profile/<profileName>', methods=['GET'])
def getProfileInfo(profileName):
    logger.info('Hitting URL %s', request.url)

    error, response = None, None
    appData = AppDataCore.getAppData()
    response = appData['profile'].get(profileName, None)

    if response == None:
        error = 'Profile %s does not exist.' % (profileName)

    logger.debug('Error: %s', error)
    logger.debug('Response: %s', response)
    return jsonify(response=response, error=error)