# Generated by Django 2.2.6 on 2019-10-11 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_fname', models.CharField(max_length=200)),
                ('author_lname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Author'),
            preserve_default=False,
        ),
    ]