# Generated by Django 4.0.6 on 2022-08-24 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_u_id_users_login_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_login',
            old_name='uid',
            new_name='uid2',
        ),
    ]
