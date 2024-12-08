# Generated by Django 5.1.3 on 2024-12-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0008_alter_claim_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='end_time',
            field=models.DateTimeField(db_index=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='format',
            field=models.CharField(choices=[('ONLINE', 'Онлайн'), ('OFFLINE', 'Оффлайн'), ('ONLINE/OFFLINE', 'Онлайн/Оффлайн')], db_index=True, default='ONLINE', max_length=20, verbose_name='Формат соревнования'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name='Название заявки'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='place',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='start_time',
            field=models.DateTimeField(db_index=True, null=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новый'), ('ONPROGRESS', 'На рассмотрении'), ('MODERATE', 'Отправлен на модерацию'), ('REJECTED', 'Отклонен'), ('ACCEPTED', 'Принят')], db_index=True, default='NEW', max_length=25, verbose_name='Статус'),
        ),
    ]
