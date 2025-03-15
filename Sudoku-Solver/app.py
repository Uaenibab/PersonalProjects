#!/usr/bin/env python3

from flask import Flask, jsonify, abort, request, make_response
from flask_restful import Resource, Api
import json
import solver

import settings # Our server and db settings, stored in settings.py

app = Flask(__name__, static_url_path='/static')
api = Api(app)


####################################################################################
#
# Error handlers
#
@app.errorhandler(400) # decorators to add to 400 response
def not_found(error):
    return make_response(jsonify( { "status": "Bad request" } ), 400)

@app.errorhandler(404) # decorators to add to 404 response
def not_found(error):
    return make_response(jsonify( { "status": "Resource not found" } ), 404)

####################################################################################
#
# Static Endpoints for humans
#
class Root(Resource):
   # get method. What might others be aptly named? (hint: post)
    def get(self):
        return app.send_static_file('solver.html')

api.add_resource(Root,'/')
####################################################################################
#
# schools routing: GET and POST, individual school access
#
class Solver(Resource):
    def post(self):
        if not request.json or not 'values' in request.json:
            abort(400) # bad request
        cells = request.json['values']
        result = solver.solve(cells)
        if(not result):
            return make_response(jsonify({"Message": "Invalid Sudoku Board"}), 200)
        return make_response(jsonify({"values": result}), 200)

api = Api(app)
api.add_resource(Solver, '/solver')


#############################################################################
# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
#    app.run(host="cs3103.cs.unb.ca", port=xxxx, debug=True)
    app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=settings.APP_DEBUG)
