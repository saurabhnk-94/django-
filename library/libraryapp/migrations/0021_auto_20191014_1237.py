# Generated by Django 2.2.6 on 2019-10-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0020_auto_20191014_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.IntegerField(verbose_name='regex'),
        ),
    ]