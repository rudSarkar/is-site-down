"""
Project: Is site down
Author: Rudra Sarkar 🦸‍♂️
Twitter: @rudr4_sarkar
"""

from os import environ
from IsSiteDown import app

if __name__ == '__main__':
    app.secret_key = "super secret key"
    app.debug = True
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
