# Generated by Django 4.0.6 on 2022-09-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_rename_t_id_items_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depart',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='item',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='s_items',
            name='item',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
