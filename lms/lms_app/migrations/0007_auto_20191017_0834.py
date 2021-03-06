# Generated by Django 2.2.6 on 2019-10-17 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0006_auto_20191017_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='record',
            name='date_of_return',
            field=models.DateField(default=datetime.datetime(2019, 10, 24, 8, 34, 3, 499190)),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 17, 8, 34, 3, 499165)),
        ),
    ]
