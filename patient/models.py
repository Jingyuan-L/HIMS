# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Billing(models.Model):
    b_id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    treat = models.ForeignKey('Treatment', models.DO_NOTHING)
    due_date = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Billing'


class Doctor(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', default=1)
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    hiredate = models.DateTimeField()
    hospital = models.ForeignKey('Hospital', models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Doctor'




class Hospital(models.Model):
    hospital_id = models.SmallAutoField(primary_key=True)
    hospital_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Hospital'



class IcdTable(models.Model):
    icd_code = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=300)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'IcdTable'



class InPatient(models.Model):
    ap_id = models.OneToOneField('PatAppointment', models.DO_NOTHING, primary_key=True,db_column='ap_id')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    tbl_last_dt = models.DateTimeField()
    room = models.ForeignKey('Room', models.DO_NOTHING)

    class Meta:
        db_table = 'InPatient'



class InsuranceProvider(models.Model):
    ins_p_id = models.SmallAutoField(primary_key=True)
    ins_provider_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'InsuranceProvider'

class Ins_Pat(models.Model):
    ins_p_id = models.ForeignKey('InsuranceProvider', models.DO_NOTHING,db_column='ins_p_id')
    p_id = models.ForeignKey('Patient', models.DO_NOTHING,db_column='p_id')
    insurance_id = models.IntegerField(auto_created=True)
    tbl_last_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Ins_Pat'
        unique_together = ("ins_p_id", "p_id")


class Lab(models.Model):
    lab_id = models.SmallAutoField(primary_key=True)
    lab_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Lab'


class LabResult(models.Model):
    test_id = models.BigAutoField(primary_key=True)
    test_description = models.CharField(max_length=120)
    test_result = models.CharField(max_length=30)
    lab = models.ForeignKey(Lab, models.DO_NOTHING)
    treat = models.ForeignKey('Treatment', models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'LabResult'


class NonMedicalStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    hiredate = models.DateTimeField()
    type = models.CharField(max_length=30)
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'NonMedicalStaff'


class NursHmPatient(models.Model):
    ap_id = models.OneToOneField('PatAppointment', models.DO_NOTHING, primary_key=True,db_column='ap_id')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'NursHmPatient'


class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    hiredate = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Nurse'


class OutPatient(models.Model):
    ap_id = models.OneToOneField('PatAppointment', models.DO_NOTHING, primary_key=True,db_column='ap_id')
    treated_time = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'OutPatient'


class PatAppointment(models.Model):
    STATUS = (
        ('processing','processing'),
        ('further operation','further operation'),
        ('end', 'end')
    )

    ap_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey('Patient', models.DO_NOTHING,db_column='p_id')
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING,db_column='doctor')
    ins_p_id = models.ForeignKey(InsuranceProvider, models.DO_NOTHING,default=1,db_column='ins_p_id')
    ap_time = models.DateTimeField()
    status = models.CharField(max_length=30,choices=STATUS, default='processing')
    last_ap = models.ForeignKey('PatAppointment', models.DO_NOTHING,blank=True, null=True,db_column='last_ap')
    type = models.CharField(max_length=30,default='outpatient')
    tbl_last_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PatAppointment'


class Patient(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user',default=1)
    p_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30,blank=True, null=True)
    last_name = models.CharField(max_length=30,blank=True, null=True)
    state = models.CharField(max_length=2,blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    street_address = models.CharField(max_length=120,blank=True, null=True)
    zip_code = models.CharField(max_length=30,blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    e_mail = models.CharField(max_length=30,blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    tbl_last_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Patient'


class Receipt(models.Model):
    rcpt_id = models.BigAutoField(primary_key=True)
    payment_date = models.DateTimeField()
    payment_amout = models.DecimalField(max_digits=8, decimal_places=2)
    b = models.ForeignKey(Billing, models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Receipt'


class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    room_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)
    tbl_last_dt = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING)

    class Meta:
        db_table = 'Room'


class Treatment(models.Model):
    treat_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=300)
    ap = models.ForeignKey(PatAppointment, models.DO_NOTHING)
    icd_code = models.ForeignKey(IcdTable, models.DO_NOTHING, db_column='icd_code')
    treat_type = models.CharField(max_length=30)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        db_table = 'Treatment'
