# Generated by Django 2.2.18 on 2021-04-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0021_auto_20210420_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalReports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patientId', models.IntegerField()),
                ('appoId', models.IntegerField()),
                ('report', models.FileField(upload_to='')),
                ('date', models.DateField(default='00-00-0000')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=496050777289, editable=False, unique=True),
        ),
    ]
