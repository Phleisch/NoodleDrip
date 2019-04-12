from flask import Flask, render_template, request, jsonify, url_for
from collections import OrderedDict
import os
import re
import sys
import json

app = Flask(__name__)

# Error Functions / Handling

def page_not_found():
    return "Stop going to places you're not supposed to be in"

def bad_method():
    return "That's not what that endpoint is supposed to do"

def default_error():
    return "What the heck did you do?"

# List of error functions mapped to the error code they handle

error_functions = {404: page_not_found, 405: bad_method}

# Handle exception of page not being found
@app.errorhandler(Exception)
def handle_error(error):
    error_code = error.code
    print(error, sys.stderr)
    for code in error_functions:
        if code == error_code:
            return error_functions[code]()

    return default_error()

# Miscellaneous

# Home page
@app.route('/', methods=["GET"])
def get_home():
    reviews = os.listdir('reviews/')
    data = {}
    counter = 1

    for review in reviews:
        file_path = 'reviews/' + review
        key_name = 'review' + str(counter)
        data[key_name] = {}

        with open(file_path, 'r') as jsonfile:
            temp_data = jsonfile.read()

        temp_json = json.loads(temp_data, object_pairs_hook=OrderedDict)
        data[key_name]['href'] = review
        data[key_name]['albumArt'] = str(temp_json['album']['albumArt'])
        data[key_name]['albumName'] = str(temp_json['album']['title'])

        counter += 1

    jdata = json.dumps(data)
    jjdata = json.loads(jdata, object_pairs_hook=OrderedDict)
    return render_template('index.html', data=jjdata)

@app.route('/<string:review_name>', methods=["GET"])
def get_review(review_name):
    review = re.sub('[^A-Za-z0-9\-]', '', review_name)
    file_path = 'reviews/' + review + '.json'

    try:
        with open(file_path, 'r') as jsonfile:
            data = jsonfile.read()

    except IOError as ex:
        return default_error() # Should replace with 404 page

    # object_pairs_hook is for keeping track list in order since json has no order
    jdata = json.loads(data, object_pairs_hook=OrderedDict)
    return render_template('review.html', data=jdata)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
