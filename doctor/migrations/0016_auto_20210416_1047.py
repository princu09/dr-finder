# Generated by Django 2.2.18 on 2021-04-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_auto_20210416_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappoinment',
            name='approve',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=404637355162, editable=False, unique=True),
        ),
    ]