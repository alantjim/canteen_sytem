# Generated by Django 4.0.6 on 2022-08-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_rename_uid_users_login_uid2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_reg',
            name='uid',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
