# Generated by Django 3.2.3 on 2021-05-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
