import csv
import mysql.connector

'''
MySQL
'''
# config = {
#     "user": "admin",
#     "password": "12345678",
#     "host": "database-1.c4q5ttctdu2e.ap-southeast-1.rds.amazonaws.com",
# }
# config = {
#     "user": "gic",
#     "password": "gic",
#     "host": "localhost",
# }
config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
}
mysql_db = mysql.connector.connect(**config)

cursor = mysql_db.cursor()

# Drop Database
cursor.execute("DROP DATABASE IF EXISTS gic_hackathon")

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS gic_hackathon")
cursor.execute("USE gic_hackathon")

cursor.execute("CREATE TABLE IF NOT EXISTS instruments ("
               "instrumentId INT, "
               "instrumentName TEXT, "
               "instrumentType TEXT, "
               "sector TEXT, "
               "country TEXT, "
               "instrumentCurrency TEXT, "
               "isTradeable INT, "
               "createdAt DATETIME, "
               "modifiedAt DATETIME, "
               "notes TEXT,"
               "flag BOOLEAN"
               ")")

with open("instruments.csv", "r") as f:
    reader = csv.reader(f)
    columns = next(reader)
    query = "insert into instruments values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for data in reader:
        data[6] = 1 if data[6] == "True" else 0
        cursor.execute(query, data)
    mysql_db.commit()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS market_values ("
#                "instrumentId INT, "
#                "marketValueDate DATETIME, "
#                "marketValue DECIMAL, "
#                "createdAt DATETIME, "
#                "modifiedAt DATETIME"
#                ")")
#
# with open("market-values.csv", "r") as f:
#     reader = csv.reader(f)
#     columns = next(reader)
#     query = "insert into market_values values (%s, %s, %s, %s, %s)"
#     for data in reader:
#         cursor.execute(query, data)
#     mysql_db.commit()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS transactions ("
#                "transactionId INT, "
#                "instrumentId INT, "
#                "transactionAmount DECIMAL, "
#                "transactionCurrency TEXT, "
#                "transactionDate DATETIME, "
#                "quantity DECIMAL, "
#                "isCancelled INT, "
#                "createdAt DATETIME, "
#                "modifiedAt DATETIME, "
#                "transactiontype TEXT"
#                ")")
#
# with open("transactions.csv", "r") as f:
#     reader = csv.reader(f)
#     columns = next(reader)
#     query = "insert into transactions values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     for data in reader:
#         data[6] = 1 if data[6] == "True" else 0
#         cursor.execute(query, data)
#     mysql_db.commit()

mysql_db.close()

if __name__ == "__main__":
    print("Import Data")
