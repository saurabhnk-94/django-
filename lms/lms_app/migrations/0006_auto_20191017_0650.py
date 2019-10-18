# Generated by Django 2.2.6 on 2019-10-17 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_auto_20191017_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='librarian',
            new_name='librarian_name',
        ),
        migrations.RemoveField(
            model_name='record',
            name='library',
        ),
        migrations.AlterField(
            model_name='record',
            name='date_of_return',
            field=models.DateField(default=datetime.datetime(2019, 10, 24, 6, 50, 2, 680337)),
        ),
        migrations.AlterField(
            model_name='record',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 17, 6, 50, 2, 680312)),
        ),
    ]