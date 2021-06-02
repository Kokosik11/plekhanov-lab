# Generated by Django 3.2 on 2021-05-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210517_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В процессе', 'В процессе'), ('Принят', 'Принят'), ('Отменен', 'Отменен'), ('Оформлен', 'Оформлен')], default='Оформлен', max_length=100, verbose_name='Статус'),
        ),
    ]