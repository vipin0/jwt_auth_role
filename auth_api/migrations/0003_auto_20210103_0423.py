# Generated by Django 3.1.4 on 2021-01-03 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0002_auto_20210102_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]