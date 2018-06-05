'''
Created on 22.05.2018
@author: Moamen Ibrahim
    REFERENCEs:
    -   [1] Programmable Web Project course 
'''

import json

from urllib.parse import unquote

from flask import Flask, request, Response, g, _request_ctx_stack, redirect, send_from_directory
from flask_restful import Resource, Api, abort
from werkzeug.exceptions import NotFound, UnsupportedMediaType

from app.utils import RegexConverter
from app import functions
from app.model.mason import MasonObject

# Constants for hypermedia formats and profiles
MASON = "application/vnd.mason+json"
JSON = "application/json"
MORSE_PROFILE = "/morse/profiles/convert-profile/"
ERROR_PROFILE = "/morse/profiles/error-profile"

# Fill these in
# Fill with the correct Apiary url"
APIARY_PROJECT = "https://critique.docs.apiary.io"
APIARY_PROFILES_URL = APIARY_PROJECT+"/#reference/profiles/"
APIARY_RELATIONS_URL = APIARY_PROJECT+"/#reference/link-relations/"

LINK_RELATIONS_URL = "/critique/link-relations/"

# Borrowed from programable web project course 

# Define the application and the api
app = Flask(__name__, static_folder="static", static_url_path="/.")
app.debug = True
# Start the RESTFUL API.
api = Api(app)

# Borrowed from programable web project course 
@app.errorhandler(404)
def resource_not_found(error):  # Borrowed from programable web project course 

    return create_error_response(404, "Resource not found",
                                 "This resource url does not exit")


@app.errorhandler(400)
def resource_not_found(error):  # Borrowed from programable web project course 

    return create_error_response(400, "Malformed input format",
                                 "The format of the input is incorrect")

@app.errorhandler(500)
def unknown_error(error):  # Borrowed from programable web project course 

    return create_error_response(500, "Error",
                                 "The system has failed. Please, contact the administrator")


class MorseRequests(Resource):

    def get(self):
        '''
        get resource method (fetching results)
        '''
        pass

    def post(self):
        '''
        post resource method (adding files)
        '''
        pass

    def put(self):
        '''
        put resource method  (editing files)
        '''
        pass 

    def delete(self):
        '''
        delete reource method (mostly for deleting files)
        '''
        pass 


# Add the Regex Converter so we can use regex expressions when we define the
# routes
# Borrowed from programable web project course 
app.url_map.converters["regex"] = RegexConverter


# Define the routes
api.add_resource(morse, "/morse/api/convert/",
                 endpoint="convert")

# Borrowed from programable web project course 
@app.route("/morse/profiles/<profile_name>/")
def redirect_to_profile(profile_name):
    return redirect(APIARY_PROFILES_URL + profile_name)


# Borrowed from programable web project course 
@app.route("/morse/link-relations/<rel_name>/")
def redirect_to_relations(rel_name):
    return redirect(APIARY_RELATIONS_URL + rel_name)

# Start the application
# DATABASE SHOULD HAVE BEEN POPULATED PREVIOUSLY
if __name__ == '__main__':  # Borrowed from programable web project course 
    # Debug true activates automatic code reloading and improved error messages
    app.run(debug=True)
