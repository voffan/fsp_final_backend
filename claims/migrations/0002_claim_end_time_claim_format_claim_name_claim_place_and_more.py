# Generated by Django 5.1.3 on 2024-12-06 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='claim',
            name='format',
            field=models.CharField(choices=[('ONLINE', 'Онлайн'), ('OFFLINE', 'Оффлайн'), ('ONLINE/OFFLINE', 'Онлайн/Оффлайн')], default='ONLINE', max_length=20, verbose_name='Формат соревнования'),
        ),
        migrations.AddField(
            model_name='claim',
            name='name',
            field=models.CharField(max_length=25, null=True, verbose_name='Название заявки'),
        ),
        migrations.AddField(
            model_name='claim',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='claim',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='Дата начала'),
        ),
        migrations.CreateModel(
            name='ClaimFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.claim', verbose_name='Заявка')),
            ],
        ),
    ]
