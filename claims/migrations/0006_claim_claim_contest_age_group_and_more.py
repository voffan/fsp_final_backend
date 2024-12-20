# Generated by Django 5.1.3 on 2024-12-07 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0005_claim_receiver_federation_claim_sender_federation'),
        ('contests', '0005_contest_contest_char_alter_contest_format_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='claim_contest_age_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.agegroup', verbose_name='Возрастная группа'),
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_contest_char',
            field=models.CharField(choices=[('Линчная', 'Личная'), ('Командная', 'Командная')], db_index=True, default='Линчная', max_length=11, verbose_name='Характер соревнования'),
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_contest_discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.discipline', verbose_name='Дисциплина соревнования'),
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_contest_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.contesttype', verbose_name='Уровень соревнования'),
        ),
    ]
