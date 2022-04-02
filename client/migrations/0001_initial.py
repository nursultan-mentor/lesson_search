# Generated by Django 4.0.1 on 2022-04-02 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Продукт кредитования')),
                ('interest_rate', models.FloatField(default=28, verbose_name='Процентная ставка')),
                ('max_sum', models.IntegerField(default=100000, verbose_name='Сумма 1')),
                ('commission', models.FloatField(default=0, verbose_name='Комиссия за выдачу')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('sum', models.IntegerField()),
                ('status', models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Одобрен', 'Одобрен'), ('Отказано', 'Отказано')], max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.product')),
            ],
        ),
    ]