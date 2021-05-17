# Generated by Django 3.2 on 2021-05-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Отменен', 'Отменен'), ('Оформлен', 'Оформлен'), ('Принят', 'Принят'), ('В процессе', 'В процессе')], default='Оформлен', max_length=100, verbose_name='Статус'),
        ),
    ]
