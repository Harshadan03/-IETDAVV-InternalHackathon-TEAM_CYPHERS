# Generated by Django 2.2.6 on 2020-01-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0006_tribalskills_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribalskills',
            name='img',
            field=models.ImageField(upload_to='skillpics/'),
        ),
    ]
