# Generated by Django 3.2 on 2021-06-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Оформлен', 'Оформлен'), ('Отменен', 'Отменен'), ('В процессе', 'В процессе'), ('Принят', 'Принят')], default='Оформлен', max_length=100, verbose_name='Статус'),
        ),
    ]