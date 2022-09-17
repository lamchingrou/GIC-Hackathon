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

@application.route("/", methods=["GET"])
@cross_origin()
def Index():
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("USE gic_hackathon")
    cursor.execute("SELECT * FROM instruments WHERE flag")
    list_of_instruments = cursor.fetchall()
    return render_template('index.html', list_of_instruments = list_of_instruments)

@application.route("/add", methods=["POST"])
@cross_origin()
def add_instruments_list():
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    instrumentName = request.form['instrumentName']
    instrumentType = request.form['instrumentType']
    country = request.form['country']
    sector = request.form['sector']
    instrumentCurrency = request.form['instrumentCurrency']
    isTradeable = request.form['isTradeable']
    createdAt = datetime.now()
    modifiedAt = datetime.min()
    notes = request.form['notes']
    flag = True
    cursor.execute("INSERT INTO instruments (instrumentName, instrumentType, sector, country, instrumentCurrency, isTradeable, createdAt, modifiedAt, notes, flag) VALUES (%s, %s, %s, %s, %s, %b, %?, %?, %s, %b)", (instrumentName, instrumentType, sector, country, instrumentCurrency, isTradeable, createdAt, modifiedAt, notes, flag))
    db.close()
    flash("New instrument created!")
    return redirect(url_for('Index'))

@application.route("/getInstrument/<int:instrumentId>", methods=["GET", "POST"])
@cross_origin()
def get_instrument(instrumentId):
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("USE gic_hackathon")
    cursor.execute("SELECT * FROM instruments WHERE instrumentId = %d", (instrumentId))
    instrument_by_id = cursor.fetchall()
    db.close()
    return render_template('view.html', instrument_by_id = instrument_by_id)

@application.route("/edit/<int:instrumentId>", methods=["POST"])
@cross_origin()
def edit_instrument(instrumentId):
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    instrumentName = request.form['instrumentName']
    instrumentType = request.form['instrumentType']
    country = request.form['country']
    sector = request.form['sector']
    instrumentCurrency = request.form['instrumentCurrency']
    isTradeable = request.form['isTradeable']
    modifiedAt = datetime.now()
    notes = request.form['notes']
    cursor.execute("UPDATE instruments SET instrumentName = %s, instrumentType = %s, sector = %s, country = %s, instrumentCurrency = %s, isTradeable = %b, modifiedAt = %?, notes = %s) WHERE instrumentId = %d", (instrumentName, instrumentType, sector, country, instrumentCurrency, isTradeable, modifiedAt, notes, instrumentId))
    flash("Successfully updated instrument!")
    db.commit()
    return redirect(url_for('Index'))

@application.route("/delete/<int:instrumentId>", methods=["GET", "POST"])
@cross_origin()
def delete_instrument(instrumentId):
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    flag = False
    cursor.execute("UPDATE instruments SET flag = %b WHERE instrumentId = %d", (flag, instrumentId))
    flash("Successfully deleted instrument!")
    db.commit()
    return redirect(url_for('Index'))

if __name__ == "__main__":
   
    application.debug = True
    # application.run(host="0.0.0.0", port=5000)
    application.run()