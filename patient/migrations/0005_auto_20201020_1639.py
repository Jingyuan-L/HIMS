# Generated by Django 3.1.1 on 2020-10-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20201019_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='receipt',
            name='pay_method',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('PayPal', 'PayPal')], default='Credit Card', max_length=30),
        ),
    ]