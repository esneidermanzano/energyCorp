# Generated by Django 3.0.3 on 2020-05-18 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0008_auto_20200518_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='paymentdeadlineInvoice',
            field=models.DateField(default=datetime.datetime(2020, 5, 28, 23, 44, 43, 210616)),
        ),
    ]
