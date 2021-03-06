# Generated by Django 3.2.13 on 2022-07-02 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0004_delete_instrument_manager'),
        ('accounts', '0005_delete_instrument_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrument.instrument')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
