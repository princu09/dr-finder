# Generated by Django 3.2.5 on 2021-11-03 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0026_alter_healthcard_hcno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HealthCard',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='healthCard',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='healthCardAcceptByAdmin',
        ),
    ]