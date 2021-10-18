# Generated by Django 2.2.18 on 2021-04-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_auto_20210410_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthcard',
            old_name='userName',
            new_name='userFName',
        ),
        migrations.AddField(
            model_name='healthcard',
            name='userLName',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='hcNo',
            field=models.IntegerField(default=4757355403251219, editable=False, unique=True),
        ),
    ]
