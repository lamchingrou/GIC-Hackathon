import mysql.connector

config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
}

if __name__ == "__main__":
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("USE gic_hackathon")
    cursor.execute("SELECT * FROM instruments")
    result = cursor.fetchall()
    db.close()
    print(result)
