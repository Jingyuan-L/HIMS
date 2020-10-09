import MySQLdb
from faker import Faker

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="admin",
                     db="hims_oltp_db",
                     port=3306,
                     )
cur = db.cursor()

