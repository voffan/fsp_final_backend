# Generated by Django 5.1.3 on 2024-12-07 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0004_alter_agegroup_end'),
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=300, verbose_name='ФИО')),
                ('age_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.agegroup', verbose_name='Возрастная группа')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('members', models.ManyToManyField(to='contestant.contestant', verbose_name='Члены команды')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.region', verbose_name='Регион')),
            ],
        ),
    ]
