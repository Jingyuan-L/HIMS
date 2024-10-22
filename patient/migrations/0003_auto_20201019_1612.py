# Generated by Django 3.1.1 on 2020-10-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20201019_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='e_mail',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='street_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
