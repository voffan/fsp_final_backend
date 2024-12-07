# Generated by Django 5.1.3 on 2024-12-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0006_claim_claim_contest_age_group_and_more'),
        ('contests', '0005_contest_contest_char_alter_contest_format_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='claim_contest_char',
            new_name='contest_char',
        ),
        migrations.RenameField(
            model_name='claim',
            old_name='claim_contest_type',
            new_name='contest_type',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='claim_contest_age_group',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='claim_contest_discipline',
        ),
        migrations.AddField(
            model_name='claim',
            name='contest_age_group',
            field=models.ManyToManyField(to='contests.agegroup', verbose_name='Возрастная группа'),
        ),
        migrations.AddField(
            model_name='claim',
            name='contest_discipline',
            field=models.ManyToManyField(to='contests.discipline', verbose_name='Дисциплина соревнования'),
        ),
    ]