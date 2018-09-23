#! /usr/bin/env python3

"""
A simple router / controler implementation
"""

from flask import Flask
from flask import request
from flask import Response
from models.fibonacci_generator import fibonacci

__author__  = "Mindaugas Bernatavičius"
__date__    = "2018-09-22"


def create_app():
    
    app = Flask(__name__)


    @app.route("/", methods=['GET'])
    def hello():
        return "Welcome to the Fibonacci sequence generator, use /fib?limit=10\
                to generate a 10 diggit fibonacci sequence\n"


    @app.route("/fib", methods=['GET'])
    def fib():
        # TODO :: check if the arguments even exist
        limit = request.args.get('limit')
        debug = request.args.get('debug')
        # we are streaming the results
        # to offload the origin server asap
        # and let the proxy buffer stream
        # for caching purposes
        def generate_fibs():
            for x in range(int(limit)):
                if not debug:
                    yield str(fibonacci(x)) + '\n'
                else: 
                    yield str(fibonacci(x, True)) + '\n'
        return Response(generate_fibs(), mimetype='text/plain')
        
        
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()