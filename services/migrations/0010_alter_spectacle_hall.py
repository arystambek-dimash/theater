# Generated by Django 5.0.6 on 2024-05-23 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_ticket_seat_alter_ticket_spectacle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spectacle',
            name='hall',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='spectacles', to='services.hall'),
        ),
    ]
