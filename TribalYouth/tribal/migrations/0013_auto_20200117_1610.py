# Generated by Django 2.2.6 on 2020-01-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0012_auto_20200117_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribalskills',
            name='desc',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='tribalskills',
            name='title',
            field=models.CharField(default=' ', max_length=80),
        ),
    ]
