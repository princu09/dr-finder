# Generated by Django 2.2.18 on 2021-04-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20210410_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcNo', models.IntegerField(default=4723959157426431, editable=False, unique=True)),
            ],
        ),
    ]
