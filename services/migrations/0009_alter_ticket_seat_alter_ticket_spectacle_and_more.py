# Generated by Django 5.0.6 on 2024-05-23 20:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_ticket_qr_code_alter_ticket_seat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.seat'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='spectacle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.spectacle'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
