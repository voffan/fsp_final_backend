# Generated by Django 5.1.3 on 2024-12-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_alter_agegroup_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_char',
            field=models.CharField(choices=[('Линчная', 'Личная'), ('Командная', 'Командная')], db_index=True, default='Линчная', max_length=11, verbose_name='Характер соревнования'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='format',
            field=models.CharField(choices=[('ONLINE', 'Онлайн'), ('OFFLINE', 'Оффлайн'), ('ONLINE/OFFLINE', 'Онлайн/Оффлайн')], db_index=True, default='ONLINE', max_length=20, verbose_name='Формат соревнования'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Активный'), ('CLOSED', 'Закрыт'), ('CANCLED', 'Отменен')], db_index=True, default='ACTIVE', max_length=10, verbose_name='Статус'),
        ),
    ]
