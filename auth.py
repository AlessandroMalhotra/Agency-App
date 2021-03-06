import json
import os
from urllib.request import urlopen
from functools import wraps

from flask import Flask, request, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = ["RS256"]
API_AUDIENCE = os.environ.get('API_AUDIENCE')


''' Error handler '''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


''' Auth Header for token '''
def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header """
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


''' Verifies the token '''
def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer ="https://" + AUTH0_DOMAIN + "/"
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                            "description": "token is expired"}, 401)

        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                             "description":
                             "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                             "description":
                             "Unable to parse authentication"
                                    " token."}, 401)

    raise AuthError({"code": "invalid_header",
                     "description": "Unable to find appropriate key"}, 401)


''' Check correct permissions in payload '''
def check_permissions(permission, payload):

    if 'permissions' not in payload:
        raise AuthError({'code': 'invalid_claims',
                         'description': 'Permissions not included in JWT.'}, 400)

    if permission not in payload['permissions']:
        raise AuthError({'code': 'unauthorized',
                         'description': 'Permission not found.'}, 403)

    return True


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
