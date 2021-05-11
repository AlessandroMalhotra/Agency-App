import json
from six.moves.urllib.request import urlopen
from functools import wraps

from flask import Flask, request, abort
from flask_cors import cross_origin
from jose import jwt

AUTH0_DOMAIN = 'alessandromalhotra.eu.auth0.com'
API_AUDIENCE = 'https://localhost:5050'
ALGORITHMS = ["RS256"]


# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
   """Obtains the Access Token from the Authorization Header
    """
    auth_header = request.headers.get('Authorization', None)
    
    if not auth_header:
        raise AuthError({"code": "authorization_header_missing",
        "description": "Authorization header is expected"}, 401)
    
    header_parts = auth_header.split(' ')

    if header_parts[0].lower() != 'bearer':
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    
    elif len(header_parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    
    elif len(header_parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)
    
    token = header_parts[1]
    return token

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header
        return (jwt, *args, **kwargs)
    return wrapper

