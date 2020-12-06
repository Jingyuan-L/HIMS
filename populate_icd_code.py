import MySQLdb
import csv
import datetime

db = MySQLdb.connect(host="hims-oltp-db.cpfsluvxtsqc.us-east-2.rds.amazonaws.com",
                     user="admin",
                     passwd="12345678",
                     db="hims_oltp_db",
                     port=3306,
                     )
cur = db.cursor()
sql = "INSERT INTO IcdTable(icd_code, description, tbl_last_dt) VALUES(%s, %s, now())"

icd_file_name = 'categories.csv'
with open(icd_file_name) as csv_file:
    reader = csv.reader(csv_file)
    FLAG = True
    for line in reader:
        param = (line[0], line[1])
        n = cur.execute(sql, param)
        if not n:
            FLAG = False

    cur.close()

    if FLAG:
        db.commit()
    else:
        db.rollback()

    db.close()
