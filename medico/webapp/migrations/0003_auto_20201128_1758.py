# Generated by Django 3.1 on 2020-11-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20201128_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, default='logoo.png', null=True, upload_to=''),
        ),
    ]