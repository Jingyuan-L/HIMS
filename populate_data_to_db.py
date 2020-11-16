import MySQLdb
import datetime as dt
from faker import Faker

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="admin",
                     db="hims_oltp_db",
                     port=3306,
                     )
cur = db.cursor()
f = Faker()

# Step 1: independent table: hospital, insuranceprovider, lab
# sql_hospital = "INSERT INTO hospital()"


# Step 2: single dependency topological order:
# a. user --> patient
# b. hospital --> doctor, nurse, nonmedicalstaff, room,

# Step 3: multiple dependencies topological order:
# c. insuranceprovider, patient --> ins_pat
# d. ins_pat, patient, doctor --> patappointment --> treatment --> billing --> receipt
# e. patappointment, room --> inpatient
# f. patappointment --> nushmpatient
# g. patappointment, treatment(time) --> outpatient
# h. treatment, lab --> labresult


sql_user = "INSERT INTO auth_user(username, password, email, is_superuser, first_name, last_name, is_staff, " \
           "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
sql_patient = "INSERT INTO patient(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

sql_doctor = "INSERT INTO doctor(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user, hospital_id)" \
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
sql_appointment = "INSERT INTO patappointment(status, type, doctor, ins_p_id, p_id) VALUES (%s, %s, %s, %s, %s)"





profile = f.simple_profile()

param = (profile['username'], f.password(), profile['mail'], 0, profile['name'].split()[0], profile['name'].split()[1], 0, 1, dt.datetime.now())
cur.execute(sql_user, param)
id = cur.lastrowid
param = (profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
         profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
         profile['address'].split('\n')[1].split(',')[1].split()[1],
         int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'], id)
cur.execute(sql_patient, param)

cur.close()
db.commit()
db.close()