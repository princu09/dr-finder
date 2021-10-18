# Generated by Django 2.2.18 on 2021-04-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_auto_20210416_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappoinment',
            name='doctorId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=452383763838, editable=False, unique=True),
        ),
    ]