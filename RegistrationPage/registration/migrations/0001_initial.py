# Generated by Django 2.1 on 2019-04-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField(max_length=8)),
                ('phone_number', models.TextField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=1024)),
                ('zip_code', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=10)),
                ('hospital_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20, unique=True)),
                ('phone_number1', models.TextField(max_length=10)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('mediciene_name', models.CharField(max_length=100)),
                ('mediciene_power', models.CharField(max_length=10)),
                ('dose', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=10)),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
    ]
