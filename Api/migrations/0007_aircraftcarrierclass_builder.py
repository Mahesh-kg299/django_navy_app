# Generated by Django 4.2.4 on 2014-04-21 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_builder_remove_aircraftcarrier_builder'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftcarrierclass',
            name='builder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='Api.builder'),
            preserve_default=False,
        ),
    ]
