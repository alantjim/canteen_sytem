# Generated by Django 4.0.6 on 2022-09-23 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_alter_items_type_alter_s_items_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='s_items',
            name='person',
        ),
    ]
