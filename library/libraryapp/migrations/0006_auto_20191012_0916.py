# Generated by Django 2.2.6 on 2019-10-12 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_auto_20191011_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]