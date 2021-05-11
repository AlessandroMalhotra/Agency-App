import json
from six.moves.urllib.request import urlopen
from functools import wraps

from flask import Flask, request, abort
from flask_cors import cross_origin
from jose import jwt

AUTH0_DOMAIN = 'alessandromalhotra.eu.auth0.com'
API_AUDIENCE = 'https://localhost:5050'
ALGORITHMS = ["RS256"]

def get_token_auth_header():
   """Obtains the Access Token from the Authorization Header
    """
    auth_header = request.headers.get('Authorization', None)
    if not 
    
    header_parts = auth_header.split(' ')

    if len(header_parts) != 2:
        abort(401)
    
    elif header_parts[0].lower() != 'bearer':
        abort(401)
    
    return auth_header[0]

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header
        return (jwt, *args, **kwargs)
    return wrapper

