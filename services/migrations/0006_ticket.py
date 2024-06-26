# Generated by Django 5.0.6 on 2024-05-23 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_spectacle_time_passing_delete_spectacletime'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='services.seat')),
                ('spectacle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='services.spectacle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
