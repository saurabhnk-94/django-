# Generated by Django 2.2.6 on 2019-10-17 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0011_auto_20191017_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date_of_return',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.date(2019, 10, 17)),
        ),
    ]