# Generated by Django 5.1.3 on 2024-12-07 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0005_contest_contest_char_alter_contest_format_and_more'),
        ('federations', '0002_federation_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='federation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fedration_set', to='federations.federation', verbose_name='Федерация'),
        ),
        migrations.AddField(
            model_name='contest',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizer_set', to='federations.federation', verbose_name='Организатор'),
        ),
    ]
