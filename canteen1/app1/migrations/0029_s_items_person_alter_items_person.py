# Generated by Django 4.0.6 on 2022-09-23 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_alter_items_type_alter_items_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_items',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.staff_reg'),
        ),
        migrations.AlterField(
            model_name='items',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staff_reg'),
        ),
    ]
