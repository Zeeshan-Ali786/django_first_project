# Generated by Django 3.1.7 on 2021-05-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20210517_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Batch',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='batch_abbreviation',
            new_name='department_abbreviation',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='batch_name',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='studentid',
            old_name='isbn_10',
            new_name='batch',
        ),
        migrations.RemoveField(
            model_name='studentid',
            name='isbn_12',
        ),
        migrations.AddField(
            model_name='studentid',
            name='department',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='studentid',
            name='roll_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
