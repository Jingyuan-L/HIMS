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
# for _ in range(20):
#     try:
#         sql_hospital = "INSERT INTO hospital(hospital_name, state, city, street_address, zip_code, phone, e_mail) " \
#                        "VALUES(%s, %s, %s, %s, %s, %s, %s)"
#         profile = f.simple_profile()
#         param_hos = (profile['name'] + ' Hospital', profile['address'].split('\n')[1].split(',')[1].split()[0],
#                      profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#                      profile['address'].split('\n')[1].split(',')[1].split()[1],
#                      int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
#         cur.execute(sql_hospital, param_hos)
#
#         sql_insurance = "INSERT INTO insuranceprovider(ins_provider_name, state, city, street_address, zip_code, phone, e_mail) " \
#                         "VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         profile = f.simple_profile()
#         param_ins = (profile['name'] + ' Insurance', profile['address'].split('\n')[1].split(',')[1].split()[0],
#                      profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#                      profile['address'].split('\n')[1].split(',')[1].split()[1],
#                      int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
#         cur.execute(sql_insurance, param_ins)
#
#         sql_lab = "INSERT INTO lab(lab_name, state, city, street_address, zip_code, phone, e_mail) " \
#                   "VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         profile = f.simple_profile()
#         param_lab = (profile['name'] + ' Medical Lab', profile['address'].split('\n')[1].split(',')[1].split()[0],
#                      profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#                      profile['address'].split('\n')[1].split(',')[1].split()[1],
#                      int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'],)
#         cur.execute(sql_lab, param_lab)
#     except IndexError as e:
#         print(e)
#         continue


# Step 2: single dependency topological order:
# a. user --> patient
# b. user --> doctor
# c. hospital --> doctor, nurse, nonmedicalstaff, room,
# N = 15000
# for _ in range(N):
#     try:
#         sql_user = "INSERT INTO auth_user(username, password, email, is_superuser, first_name, last_name, is_staff, " \
#                    "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
#         sql_patient = "INSERT INTO patient(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user)" \
#                       " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#
#         profile = f.simple_profile()
#         param_patient_user = (
#             profile['username'], f.password(), profile['mail'], 0, profile['name'].split()[0], profile['name'].split()[1],
#             0, 1, dt.datetime.now())
#         cur.execute(sql_user, param_patient_user)
#         id = cur.lastrowid
#         param_patient = (
#             profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
#             profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#             profile['address'].split('\n')[1].split(',')[1].split()[1],
#             int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'], id)
#         cur.execute(sql_patient, param_patient)
#     except IndexError as e:
#         print(e)
#         continue
#     except MySQLdb.IntegrityError as e:
#         print(e)
#         continue
#     except MySQLdb.DataError as e:
#         print(e)
#         continue

# N = 400
# for i in range(N):
#     try:
#         sql_user = "INSERT INTO auth_user(username, password, email, is_superuser, first_name, last_name, is_staff, " \
#                    "is_active, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
#         sql_doctor = "INSERT INTO doctor(first_name, last_name, state, city, street_address, zip_code, phone, e_mail, user, hospital_id)" \
#                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#
#         profile = f.simple_profile()
#         param_doctor_user = (
#             profile['username'], f.password(), profile['mail'], 0, profile['name'].split()[0], profile['name'].split()[1],
#             1, 1, dt.datetime.now())
#         cur.execute(sql_user, param_doctor_user)
#         id = cur.lastrowid
#         cur.execute("SELECT hospital_id FROM hospital;")
#         hospital_ids = []
#         for hos_id in cur.fetchall():
#             hospital_ids.append(int(hos_id[0]))
#         if i == 0:
#             print(hospital_ids)
#         param_doctor = (
#             profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
#             profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#             profile['address'].split('\n')[1].split(',')[1].split()[1],
#             int("".join(filter(lambda c: c in "1234567890", f.phone_number()))), profile['mail'], id, random.choice(hospital_ids))
#         cur.execute(sql_doctor, param_doctor)
#
#         sql_staff = "INSERT INTO nonmedicalstaff(first_name, last_name, state, city, street_address, zip_code, " \
#                     "phone, e_mail, hospital_id, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         profile = f.simple_profile()
#         staff_type = ["accouter", "cashier", "department manager", "intern", "dean", "cleaner", "administrative staff"]
#         param_staff = (
#             profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
#             profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#             profile['address'].split('\n')[1].split(',')[1].split()[1],
#             int("".join(filter(lambda c: c in "1234567890", f.phone_number()))),
#             profile['mail'], random.choice(hospital_ids), random.choice(staff_type))
#         cur.execute(sql_staff, param_staff)
#
#         sql_nurse = "INSERT INTO nurse (first_name, last_name, state, city, street_address, zip_code, " \
#                     "phone, e_mail, hospital_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         profile = f.simple_profile()
#         param_nurse = (
#             profile['name'].split()[0], profile['name'].split()[1], profile['address'].split('\n')[1].split(',')[1].split()[0],
#             profile['address'].split('\n')[1].split(',')[0], profile['address'].split('\n')[0],
#             profile['address'].split('\n')[1].split(',')[1].split()[1],
#             int("".join(filter(lambda c: c in "1234567890", f.phone_number()))),
#             profile['mail'], random.choice(hospital_ids))
#         cur.execute(sql_nurse, param_nurse)
#
#         rooms_num = range(100)
#         alpha_list = [chr(i).upper() for i in range(97,123)]
#         sql_room = "INSERT INTO room(room_name, hospital_id, occupied) VALUES (%s, %s, %s)"
#         param_room = (random.choice(alpha_list) + str(random.choice(rooms_num)),
#                       random.choice(hospital_ids), random.choice([0, 1]))
#         cur.execute(sql_room, param_room)
#
#     except IndexError as e:
#         print(e)
#         continue
#     except MySQLdb.IntegrityError as e:
#         print(e)
#         continue
#     except MySQLdb.DataError as e:
#         print(e)
#         continue


# Step 3: multiple dependencies topological order:
# c. insuranceprovider, patient --> ins_pat
# d. ins_pat, patient, doctor --> patappointment --> treatment --> billing --> receipt
# e. patappointment, room --> inpatient
# f. patappointment --> nushmpatient
# g. patappointment, treatment(time) --> outpatient
# h. treatment, lab --> labresult

sql_ins_pat = "INSERT INTO ins_pat(insurance_id, )"




sql_appointment = "INSERT INTO patappointment(status, type, doctor, ins_p_id, p_id) VALUES (%s, %s, %s, %s, %s)"

cur.execute()

cur.close()
db.commit()
db.close()
