# Generated by Django 2.2.18 on 2021-04-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_auto_20210416_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappoinment',
            name='complateAppoinment',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=440932435804, editable=False, unique=True),
        ),
    ]