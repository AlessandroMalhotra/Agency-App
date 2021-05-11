def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)
    
    auth_header = request.headers.get('Authorization', None)
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

