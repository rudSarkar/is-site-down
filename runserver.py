"""
Project: Is site down
Author: Rudra Sarkar 🦸‍♂️
Twitter: @rudr4_sarkar
"""

from os import environ
from IsSiteDown import app

if __name__ == '__main__':
    app.secret_key = "super secret key"
    app.run()
