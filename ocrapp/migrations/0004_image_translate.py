# Generated by Django 3.2.3 on 2021-06-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0003_rename_caption_image_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='translate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
