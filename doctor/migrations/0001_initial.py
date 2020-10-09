# Generated by Django 3.1.1 on 2020-10-09 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('b_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'billing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False)),
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
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.SmallIntegerField(primary_key=True, serialize=False)),
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
                'db_table': 'hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IcdTable',
            fields=[
                ('icd_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('disease_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'icd_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('ins_p_id', models.SmallIntegerField(primary_key=True, serialize=False)),
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
                'db_table': 'insurance_provider',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.SmallIntegerField(primary_key=True, serialize=False)),
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
                'db_table': 'lab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('test_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('test_description', models.CharField(max_length=120)),
                ('test_result', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'lab_result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NonMedicalStaff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
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
            ],
            options={
                'db_table': 'non_medical_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('nurse_id', models.IntegerField(primary_key=True, serialize=False)),
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
                'db_table': 'nurse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatAppointment',
            fields=[
                ('ap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ap_time', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'pat_appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('member_insurance_id', models.CharField(max_length=30)),
                ('register_date', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('rcpt_id', models.BigIntegerField(db_column='rcpt__id', primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField()),
                ('payment_amout', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'receipt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treat_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('treat_type', models.CharField(max_length=30)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'treatment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InPatient',
            fields=[
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='doctor.patient')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'in_patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NursHmPatient',
            fields=[
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='doctor.patient')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'nurs_hm_patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OutPatient',
            fields=[
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='doctor.patient')),
                ('treated_time', models.DateTimeField()),
                ('tbl_last_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'out_patient',
                'managed': False,
            },
        ),
    ]
