import mysql.connector

config = {
  'user': 'root',
  'password': 'your_password',
  'host': 'your_host',
  'database': 'your_db_name'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()