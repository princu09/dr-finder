# Generated by Django 2.2.18 on 2021-04-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20210410_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='healthCardAcceptByAdmin',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=4229801295788964, editable=False, unique=True),
        ),
    ]
