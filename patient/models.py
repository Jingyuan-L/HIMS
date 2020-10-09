# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Billing(models.Model):
    b_id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    treat = models.ForeignKey('Treatment', models.DO_NOTHING)
    due_date = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'billing'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
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
        managed = False
        db_table = 'doctor'


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
        managed = False
        db_table = 'hospital'


class IcdTable(models.Model):
    icd_code = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=300)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'icd_table'


class InPatient(models.Model):
    p = models.OneToOneField('Patient', models.DO_NOTHING, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    tbl_last_dt = models.DateTimeField()
    room = models.ForeignKey('Room', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'in_patient'


class InsuranceProvider(models.Model):
    ins_p_id = models.SmallAutoField(primary_key=True)
    ins_provider_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    ap = models.ForeignKey('PatAppointment', models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'insurance_provider'


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
        managed = False
        db_table = 'lab'


class LabResult(models.Model):
    test_id = models.BigAutoField(primary_key=True)
    test_description = models.CharField(max_length=120)
    test_result = models.CharField(max_length=30)
    lab = models.ForeignKey(Lab, models.DO_NOTHING)
    treat = models.ForeignKey('Treatment', models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lab_result'


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
        managed = False
        db_table = 'non_medical_staff'


class NursHmPatient(models.Model):
    p = models.OneToOneField('Patient', models.DO_NOTHING, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nurs_hm_patient'


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
        managed = False
        db_table = 'nurse'


class OutPatient(models.Model):
    p = models.OneToOneField('Patient', models.DO_NOTHING, primary_key=True)
    treated_time = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'out_patient'


class PatAppointment(models.Model):
    ap_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Patient', models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING)
    ap_time = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pat_appointment'


class Patient(models.Model):
    p_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length=30)
    member_insurance_id = models.CharField(max_length=30)
    register_date = models.DateTimeField()
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'patient'


class Receipt(models.Model):
    rcpt_id = models.BigAutoField(primary_key=True)
    payment_date = models.DateTimeField()
    payment_amout = models.DecimalField(max_digits=8, decimal_places=2)
    b = models.ForeignKey(Billing, models.DO_NOTHING)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'receipt'


class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    room_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)
    tbl_last_dt = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room'


class Treatment(models.Model):
    treat_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=300)
    ap = models.ForeignKey(PatAppointment, models.DO_NOTHING)
    icd_code = models.ForeignKey(IcdTable, models.DO_NOTHING, db_column='icd_code')
    treat_type = models.CharField(max_length=30)
    tbl_last_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'treatment'
