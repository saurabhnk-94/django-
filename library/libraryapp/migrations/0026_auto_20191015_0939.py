# Generated by Django 2.2.6 on 2019-10-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0025_auto_20191015_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.BooleanField(),
        ),
    ]