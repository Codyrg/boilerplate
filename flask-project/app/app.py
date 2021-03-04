from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import render_template

import constants
import logging

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

SECRET_KEY = env.get(constants.SECRET_KEY)

app = Flask(__name__, static_folder='static')
app.secret_key = SECRET_KEY
app.debug = True

logging.basicConfig(level=logging.INFO)

@app.errorhandler(Exception)
def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response

@app.route("/")
def index():

    try:
        return render_template('index.html')
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=env.get('PORT', 3000), use_reloader=False)

