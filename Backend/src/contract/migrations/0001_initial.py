# Generated by Django 3.0.3 on 2020-05-14 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceServices',
            fields=[
                ('codeInvoice', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumptiondaysInvoice', models.PositiveIntegerField()),
                ('paymentdeadlineInvoice', models.DateField()),
                ('billingdateInvoice', models.DateField(default=datetime.date.today)),
                ('stateInvoice', models.BooleanField(default=False)),
                ('referencecodeInvoice', models.CharField(max_length=30)),
                ('total', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='users.Client')),
            ],
        ),
    ]