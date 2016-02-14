import json
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

def appconnection(f):
    def wrapped_function(*args, **kwargs):
        if request.method == 'OPTIONS':
            resp = current_app.make_default_options_response()
            resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            resp.headers['Access-Control-Allow-Headers'] = request.environ['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
        else:
            if request.data:
                input = json.loads(request.data)
            else:
                input = json.loads('{}')

            print 'Recieved:', input
            result_d = {"error" : False}
            try:
                f(input, result_d)
            except Exception as e:
                print ">> Error >>", e
                result_d["error"] = True
            result = str(json.dumps(result_d))
            print 'Returning:', result
            resp = make_response(result)

        resp.headers['Access-Control-Allow-Origin'] = request.environ.get('HTTP_ORIGIN','*')
        resp.headers['Access-Control-Allow-Cedentials'] = 'true'
        resp.headers['Access-Control-Allow-Max-Age'] = '86400'

        #print resp.response
        #print resp.headers
        return resp
    return update_wrapper(wrapped_function, f)
