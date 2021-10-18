# Generated by Django 2.2.18 on 2021-04-20 16:41

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_auto_20210416_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appoId', models.IntegerField()),
                ('tblName', jsonfield.fields.JSONField(default=dict)),
                ('qty', jsonfield.fields.JSONField(default=dict)),
                ('days', jsonfield.fields.JSONField(default=dict)),
                ('tblTime', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.AddField(
            model_name='bookappoinment',
            name='patientId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=467343830741, editable=False, unique=True),
        ),
    ]