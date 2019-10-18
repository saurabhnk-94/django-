# Generated by Django 2.2.6 on 2019-10-16 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0033_auto_20191016_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 7, 24, 8, 436115)),
        ),
        migrations.AlterField(
            model_name='record',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 23, 7, 24, 8, 436143)),
        ),
    ]