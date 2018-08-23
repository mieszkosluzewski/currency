# Generated by Django 2.1 on 2018-08-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('currency', models.CharField(max_length=3)),
                ('exchange_rate', models.FloatField()),
            ],
        ),
    ]
