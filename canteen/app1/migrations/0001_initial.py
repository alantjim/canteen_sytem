# Generated by Django 4.0.6 on 2022-09-25 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField(verbose_name=2)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('Tea_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=15)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='type',
            fields=[
                ('T_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(null=True, upload_to='type/%m')),
            ],
        ),
        migrations.CreateModel(
            name='users_login',
            fields=[
                ('uid2', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='users_reg',
            fields=[
                ('uid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('depart', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='s_items',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=15, unique=True)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='s_items/%m')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staff_reg')),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('I_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=15, unique=True)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='items/%m')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.type')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staff_reg')),
            ],
        ),
    ]
