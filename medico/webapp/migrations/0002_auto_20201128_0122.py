# Generated by Django 3.1 on 2020-11-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient',
            new_name='patientID',
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10, null=True)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('bloodgrp', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B-'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4, null=True)),
                ('BP', models.FloatField()),
                ('temp', models.FloatField()),
                ('history', models.CharField(blank=True, max_length=200, null=True)),
                ('patientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patient')),
            ],
        ),
    ]