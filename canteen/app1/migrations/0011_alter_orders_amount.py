# Generated by Django 4.0.6 on 2022-11-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.FloatField(blank=True, default=100, null=True),
        ),
    ]
