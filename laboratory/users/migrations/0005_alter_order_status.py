# Generated by Django 3.2 on 2021-05-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Отменен', 'Отменен'), ('В процессе', 'В процессе'), ('Принят', 'Принят'), ('Оформлен', 'Оформлен')], default='Оформлен', max_length=100, verbose_name='Статус'),
        ),
    ]
