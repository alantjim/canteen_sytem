# Generated by Django 4.0.6 on 2022-09-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_alter_s_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_items',
            name='image',
            field=models.ImageField(null=True, upload_to='s_items/%m'),
        ),
    ]