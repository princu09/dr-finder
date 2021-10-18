# Generated by Django 2.2.18 on 2021-04-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20210410_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcard',
            name='userName',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='healthCard',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=4653024315241530, editable=False, unique=True),
        ),
    ]