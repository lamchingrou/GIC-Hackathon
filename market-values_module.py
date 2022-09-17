import hashlib
import mysql.connector

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

application = Flask(__name__, static_url_path="", static_folder="web")
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
}


