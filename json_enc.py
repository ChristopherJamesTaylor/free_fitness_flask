import functools
from flask import Response
# if we don't have ujson use jsonify from Flask or JsonResponse from Django
try:
    import ujson
    parser = 'ujson'
except ImportError:
    parser = 'jsonify'
    from flask import jsonify

# decorator for json encoding return
def json_enc(func):
    """ encodes object to JSON for return """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """ wrapped function """
        if parser is 'ujson':
            return Response(
                response=ujson.encode(func(*args, **kwargs)),
                status=200,
                mimetype="application/json")
        elif parser is 'jsonify':
            return Response(
                response=jsonify(func(*args, **kwargs)),
                status=200,
                mimetype="application/json")
        else:
            return Response(
                response='No Json Parser',
                status=500,
                mimetype="text/html")
    return wrapper