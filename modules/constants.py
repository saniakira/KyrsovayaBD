import mysql.connector

JSON = "data\\report.json"
DATABASE = "postofficedb"

config = {
    'user': 'root',
    'password': '135789',
    'host': 'localhost',
    'port': '3306',
    'database': f'{DATABASE}',
    'raise_on_warnings': True
}

link = mysql.connector.connect(**config)
cursor = link.cursor()
