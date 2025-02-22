# Generated by Django 3.1.1 on 2020-10-19 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('b_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'Billing',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('hiredate', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'Hospital',
            },
        ),
        migrations.CreateModel(
            name='IcdTable',
            fields=[
                ('icd_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'IcdTable',
            },
        ),
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('ins_p_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('ins_provider_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'InsuranceProvider',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'Lab',
            },
        ),
        migrations.CreateModel(
            name='PatAppointment',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False)),
                ('ap_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('processing', 'processing'), ('further operation', 'further operation'), ('end', 'end')], default='processing', max_length=30)),
                ('type', models.CharField(choices=[('outpatient', 'outpatient'), ('inpatient', 'inpatient'), ('nursinghome', 'nursinghome')], default='outpatient', max_length=30)),
                ('tbl_last_dt', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(db_column='doctor', on_delete=django.db.models.deletion.DO_NOTHING, to='patient.doctor')),
                ('ins_p_id', models.ForeignKey(db_column='ins_p_id', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.insuranceprovider')),
                ('last_ap', models.ForeignKey(blank=True, db_column='last_ap', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patappointment')),
            ],
            options={
                'db_table': 'PatAppointment',
            },
        ),
        migrations.CreateModel(
            name='NursHmPatient',
            fields=[
                ('ap_id', models.OneToOneField(db_column='ap_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patient.patappointment')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'NursHmPatient',
            },
        ),
        migrations.CreateModel(
            name='OutPatient',
            fields=[
                ('ap_id', models.OneToOneField(db_column='ap_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='OutPatient', serialize=False, to='patient.patappointment')),
                ('treated_time', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'OutPatient',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('treat_type', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
                ('ap', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patappointment')),
                ('icd_code', models.ForeignKey(db_column='icd_code', on_delete=django.db.models.deletion.DO_NOTHING, to='patient.icdtable')),
            ],
            options={
                'db_table': 'Treatment',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.hospital')),
            ],
            options={
                'db_table': 'Room',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('rcpt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField()),
                ('payment_amout', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tbl_last_dt', models.DateTimeField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.billing')),
            ],
            options={
                'db_table': 'Receipt',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('street_address', models.CharField(blank=True, max_length=120, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=30, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('tbl_last_dt', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(db_column='user', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.AddField(
            model_name='patappointment',
            name='p_id',
            field=models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient'),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('nurse_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('hiredate', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.hospital')),
            ],
            options={
                'db_table': 'Nurse',
            },
        ),
        migrations.CreateModel(
            name='NonMedicalStaff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('hiredate', models.DateTimeField()),
                ('type', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.hospital')),
            ],
            options={
                'db_table': 'NonMedicalStaff',
            },
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('test_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('test_description', models.CharField(max_length=120)),
                ('test_result', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.lab')),
                ('treat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.treatment')),
            ],
            options={
                'db_table': 'LabResult',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(db_column='user', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billing',
            name='treat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.treatment'),
        ),
        migrations.CreateModel(
            name='Ins_Pat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_id', models.IntegerField(auto_created=True)),
                ('tbl_last_dt', models.DateTimeField(auto_now=True)),
                ('ins_p_id', models.ForeignKey(db_column='ins_p_id', on_delete=django.db.models.deletion.DO_NOTHING, to='patient.insuranceprovider')),
                ('p_id', models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'db_table': 'Ins_Pat',
                'unique_together': {('ins_p_id', 'p_id')},
            },
        ),
        migrations.CreateModel(
            name='InPatient',
            fields=[
                ('ap_id', models.OneToOneField(db_column='ap_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patient.patappointment')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.room')),
            ],
            options={
                'db_table': 'InPatient',
            },
        ),
    ]
