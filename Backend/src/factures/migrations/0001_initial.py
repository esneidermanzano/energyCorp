# Generated by Django 3.0.3 on 2020-05-11 22:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('energytransfers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('codeHistory', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registryHistory', models.DateField(auto_now_add=True, unique=True)),
                ('counterHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historys', to='energytransfers.Counter')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceServices',
            fields=[
                ('codeInvoice', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumptiondaysInvoice', models.PositiveIntegerField()),
                ('paymentdeadlineInvoice', models.DateField()),
                ('billingdateInvoice', models.DateField(default=datetime.date.today)),
                ('stateInvoice', models.BooleanField(default=False)),
                ('referencecodeInvoice', models.CharField(max_length=30)),
                ('history', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='factures.History')),
            ],
        ),
    ]
