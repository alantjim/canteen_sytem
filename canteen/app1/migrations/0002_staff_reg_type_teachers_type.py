# Generated by Django 4.0.6 on 2022-09-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_reg',
            name='Type',
            field=models.CharField(default='Staff', max_length=15),
        ),
        migrations.AddField(
            model_name='teachers',
            name='Type',
            field=models.CharField(default='Teacher', max_length=15),
        ),
    ]