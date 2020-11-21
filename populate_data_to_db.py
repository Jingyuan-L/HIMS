import MySQLdb
import datetime as dt
from faker import Faker
import random

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="admin",
                     db="hims_oltp_db",
                     port=3306,
                     )
cur = db.cursor()
f = Faker()

# Step 1: independent table: hospital, insuranceprovider, lab

for _ in range(20):
    try:
        sql_hospital = "INSERT INTO hospital(hospital_name, state, city, street_address, zip_code, phone, e_mail) " \
                       "VALUES(%s, %s, %s, %s, %s, %s, %s)"
        profile = f.simple_profile()
        param_hos = (profile['name'] + ' Hospital', profile['address'].split('\n')[1].split(',')[1].split()[0],
                     profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
                     profile['address'].split('\n')[1].split(',')[1].split()[1],
                     int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
        cur.execute(sql_hospital, param_hos)

        sql_insurance = "INSERT INTO insuranceprovider(ins_provider_name, state, city, street_address, zip_code, phone, e_mail) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        profile = f.simple_profile()
        param_ins = (profile['name'] + ' Insurance', profile['address'].split('\n')[1].split(',')[1].split()[0],
                     profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
                     profile['address'].split('\n')[1].split(',')[1].split()[1],
                     int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
        cur.execute(sql_insurance, param_ins)

        sql_lab = "INSERT INTO lab(lab_name, state, city, street_address, zip_code, phone, e_mail) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        profile = f.simple_profile()
        param_lab = (profile['name'] + ' Medical Lab', profile['address'].split('\n')[1].split(',')[1].split()[0],
                     profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
                     profile['address'].split('\n')[1].split(',')[1].split()[1],
                     int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
        cur.execute(sql_lab, param_lab)
    except IndexError as e:
        print(e)
        continue

###################################################################################
# Step 2: single dependency topological order:
# a. user --> patient
# b. user --> doctor
# c. hospital --> doctor, nurse, nonmedicalstaff, room,

N = 15000
for _ in range(N):
    try:
        sql_user = "INSERT INTO auth_user(username, password, email, is_superuser, first_name, last_name, is_staff, " \
                   "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        sql_patient = "INSERT INTO patient(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user)" \
                      " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        profile = f.simple_profile()
        param_patient_user = (
            profile['username'], f.password(), profile['mail'], 0, profile['name'].split()[0], profile['name'].split()[1],
            0, 1, dt.datetime.now())
        cur.execute(sql_user, param_patient_user)
        id = cur.lastrowid
        param_patient = (
            profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
            profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
            profile['address'].split('\n')[1].split(',')[1].split()[1],
            int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'], id)
        cur.execute(sql_patient, param_patient)
    except IndexError as e:
        print(e)
        continue
    except MySQLdb.IntegrityError as e:
        print(e)
        continue
    except MySQLdb.DataError as e:
        print(e)
        continue


##########################################################################################
N = 400
for i in range(N):
    try:
        sql_user = "INSERT INTO auth_user(username, password, email, is_superuser, first_name, last_name, is_staff, " \
                   "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        sql_doctor = "INSERT INTO doctor(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user, hospital_id)" \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        profile = f.simple_profile()
        param_doctor_user = (
            profile['username'], f.password(), profile['mail'], 0, profile['name'].split()[0], profile['name'].split()[1],
            1, 1, dt.datetime.now())
        cur.execute(sql_user, param_doctor_user)
        id = cur.lastrowid
        cur.execute("SELECT hospital_id FROM hospital;")
        hospital_ids = []
        for hos_id in cur.fetchall():
            hospital_ids.append(int(hos_id[0]))
        if i == 0:
            print(hospital_ids)
        param_doctor = (
            profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
            profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
            profile['address'].split('\n')[1].split(',')[1].split()[1],
            int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'], id, random.choice(hospital_ids))
        cur.execute(sql_doctor, param_doctor)

        sql_staff = "INSERT INTO nonmedicalstaff(first_name, last_name, state, city, street_address, zip_code, " \
                    "phone, e_mail, hospital_id, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        profile = f.simple_profile()
        staff_type = ["accouter", "cashier", "department manager", "intern", "dean", "cleaner", "administrative staff"]
        param_staff = (
            profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
            profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
            profile['address'].split('\n')[1].split(',')[1].split()[1],
            int("".join(filter(lambda c: c in "1234567890", f.phone_number()))),
            profile['mail'], random.choice(hospital_ids), random.choice(staff_type))
        cur.execute(sql_staff, param_staff)

        sql_nurse = "INSERT INTO nurse (first_name, last_name, state, city, street_address, zip_code, " \
                    "phone, e_mail, hospital_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        profile = f.simple_profile()
        param_nurse = (
            profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
            profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
            profile['address'].split('\n')[1].split(',')[1].split()[1],
            int("".join(filter(lambda c: c in "1234567890", f.phone_number()))),
            profile['mail'], random.choice(hospital_ids))
        cur.execute(sql_nurse, param_nurse)

        rooms_num = range(100)
        alpha_list = [chr(i).upper() for i in range(97,123)]
        sql_room = "INSERT INTO room(room_name, hospital_id, occupied) VALUES (%s, %s, %s)"
        param_room = (random.choice(alpha_list) + str(random.choice(rooms_num)),
                      random.choice(hospital_ids), random.choice([0, 1]))
        cur.execute(sql_room, param_room)

    except IndexError as e:
        print(e)
        continue
    except MySQLdb.IntegrityError as e:
        print(e)
        continue
    except MySQLdb.DataError as e:
        print(e)
        continue

############################################################################################
# Step 3: multiple dependencies topological order:
# c. insuranceprovider, patient --> ins_pat
# d. ins_pat, patient, doctor --> patappointment --> treatment --> billing --> receipt
# e. patappointment, room --> inpatient
# f. patappointment --> nushmpatient
# g. patappointment, treatment(time) --> outpatient
# h. treatment, lab --> labresult

sql_ins_pat = "INSERT INTO ins_pat(ins_p_id, p_id) VALUES (%s, %s)"
cur.execute("SELECT ins_p_id FROM insuranceprovider;")
ins_p_ids = []
for ins_p_id in cur.fetchall():
    ins_p_ids.append(ins_p_id)
cur.execute("SELECT p_id FROM patient;")

for p_id in cur.fetchall():
    param_ins_pat = (random.choice(ins_p_ids), p_id)
    cur.execute(sql_ins_pat, param_ins_pat)

appointment_status = ['processing', 'further operation', 'end']
appointment_type = ['outpatient', 'inpatient', 'nursinghome']
sql_appointment = "INSERT INTO patappointment(status, type, doctor, ins_p_id, p_id, ap_time) VALUES (%s, %s, %s, %s, %s, %s)"

cur.execute("SELECT doctor_id FROM doctor;")
doc_ids = []
for doc_id in cur.fetchall():
    doc_ids.append(doc_id)

cur.execute("SELECT ins_p_id FROM insuranceprovider;")
ins_p_ids = []
for ins_p_id in cur.fetchall():
    ins_p_ids.append(ins_p_id)

cur.execute("SELECT p_id FROM patient;")
for p_id in cur.fetchall():
    N = random.choice(range(2, 10))
    for _ in range(N):
        param_appointment = (random.choice(appointment_status), random.choice(appointment_type), random.choice(doc_ids),
                             random.choice(ins_p_ids), p_id, f.date_time_between(start_date='-1y', end_date='now'))
        cur.execute(sql_appointment, param_appointment)

#########################################################################################################
treat_type = ["medicine", "lab test"]
sql_treatment = "INSERT INTO treatment(treat_type, ap_id, icd_code) VALUES (%s, %s, %s)"
sql_billing = "INSERT INTO billing(amount, due_date, treat_id, paid) VALUES (%s, %s, %s, %s)"
icd_code = []
cur.execute("SELECT icd_code FROM icdtable;")
for code in cur.fetchall():
    icd_code.append(code)
cur.execute("SELECT ap_id FROM patappointment;")
for ap_id in cur.fetchall():
    N = random.choice(range(1, 3))
    for _ in range(N):
        param_treatment = (random.choice(treat_type), ap_id, random.choice(icd_code))
        cur.execute(sql_treatment, param_treatment)
        treat_id = cur.lastrowid
        param_billing = (random.choice(range(50, 5000)), f.date_time_between(start_date='-1y', end_date='+1y'),
                         treat_id, random.choice([0, 1]))
        cur.execute(sql_billing, param_billing)


###################################################################################
cur.execute("SELECT b_id, amount FROM billing WHERE paid = 1;")
sql_receipt = "INSERT INTO receipt(payment_date, payment_amout, b_id, pay_method)" \
              "VALUES (%s, %s, %s, %s)"
payment_method = ['Credit Card', 'Debit Card', 'PayPal']
for b_id, amount in cur.fetchall():
    param_receipt = (dt.datetime.now(), amount, b_id, random.choice(payment_method))
    cur.execute(sql_receipt, param_receipt)

####################################################################################
# e. patappointment, room --> inpatient

cur.execute("SELECT room_id FROM room;")
room_ids = []
for room in cur.fetchall():
    room_ids.append(room)
cur.execute("SELECT ap_id, ap_time FROM patappointment WHERE type = 'inpatient';")
sql_inpatient = "INSERT INTO inpatient(ap_id, start_time, end_time, room_id)" \
                "VALUES (%s, %s, %s, %s)"
for ap_id, ap_time in cur.fetchall():
    param_inpatient = (ap_id, ap_time,
                       f.date_time_between(start_date=ap_time, end_date=ap_time+dt.timedelta(minutes=259200)),
                       random.choice(room_ids))
    try:
        cur.execute(sql_inpatient, param_inpatient)
    except MySQLdb.IntegrityError:
        print(MySQLdb.IntegrityError)
        continue

################################################################################
# f. patappointment --> nushmpatient

cur.execute("SELECT ap_id, ap_time FROM patappointment WHERE type = 'nursinghome';")
sql_nurhmpatient = "INSERT INTO nurshmpatient(ap_id, start_time, end_time) VALUES (%s, %s, %s)"
for ap_id, ap_time in cur.fetchall():
    param_nurhmpatient = (ap_id, ap_time,
                          f.date_time_between(start_date=ap_time, end_date=ap_time+dt.timedelta(minutes=259200)))
    try:
        cur.execute(sql_nurhmpatient, param_nurhmpatient)
    except MySQLdb.IntegrityError:
        print(MySQLdb.IntegrityError)
        continue

#########################################################################
# g. patappointment --> outpatient

cur.execute("SELECT ap_id, ap_time FROM patappointment WHERE type = 'outpatient';")
sql_outpatient = "INSERT INTO outpatient(ap_id, treated_time) VALUES (%s, %s)"
for ap_id, ap_time in cur.fetchall():
    param_outpatient = (ap_id, f.date_time_between(start_date=ap_time, end_date=ap_time+dt.timedelta(minutes=120)))
    try:
        cur.execute(sql_outpatient, param_outpatient)
    except MySQLdb.IntegrityError:
        print(MySQLdb.IntegrityError)
        continue

##########################################################################3
# h. treatment, lab --> labresult

cur.execute("SELECT lab_id FROM lab;")
lab = []
for n in cur.fetchall():
    lab.append(n)
cur.execute("SELECT treat_id FROM treatment WHERE treat_type = 'lab test';")
sql_labresult = "INSERT INTO labresult(test_result, lab_id, treat_id) VALUES (%s, %s, %s);"
for treat_id in cur.fetchall():
    param_labresult = (random.choice(['positive', 'negative']), random.choice(lab), treat_id)
    cur.execute(sql_labresult, param_labresult)


#######################################
# ALWAYS DEEDED!!!!!!!!!!!!!!
cur.close()
db.commit()
db.close()
