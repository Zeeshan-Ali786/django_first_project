# Generated by Django 3.1.7 on 2021-05-04 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20210504_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentid',
            old_name='isSn_10',
            new_name='isbn_10',
        ),
        migrations.RenameField(
            model_name='studentid',
            old_name='isSn_12',
            new_name='isbn_12',
        ),
    ]
