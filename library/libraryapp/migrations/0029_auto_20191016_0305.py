# Generated by Django 2.2.6 on 2019-10-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0028_auto_20191016_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='return_date',
            field=models.DateField(),
        ),
    ]