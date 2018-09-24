#! /usr/bin/env python3

"""
A simple router / controler implementation
"""

from flask import Flask
from flask import request
from flask import Response
try:
    from models.fibonacci_generator import fibonacci
except ImportError as error:
    from ..models.fibonacci_generator import fibonacci


__author__  = "Mindaugas Bernatavičius"
__date__    = "2018-09-22"


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def root():
        return "Welcome to the Fibonacci sequence generator: " +\
            "use /fib?limit=10 to generate a 10 diggit fibonacci sequence."

    @app.route("/fib", methods=['GET'])
    def fib():
        limit = request.args.get('limit')
        if limit is None:
            return Response("Please provide a URL query: /?limit=n\n",
                                            mimetype='text/plain')
            
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