# Generated by Django 5.0.6 on 2024-05-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_spectacle_age_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='spectacle',
            name='image',
            field=models.ImageField(null=True, upload_to='media/img/spectacles'),
        ),
    ]