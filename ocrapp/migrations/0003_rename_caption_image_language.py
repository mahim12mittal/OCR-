# Generated by Django 3.2.3 on 2021-05-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='caption',
            new_name='language',
        ),
    ]
