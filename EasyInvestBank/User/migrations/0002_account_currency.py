# Generated by Django 4.0.6 on 2022-09-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('EUR', 'EURO'), ('JPY', 'Japanese yen'), ('BGN', 'Bulgarian lev'), ('CZK', 'Czech krone'), ('DKK', 'Danish krone'), ('GBP', 'British pound'), ('PLN', 'Polish Zloty'), ('SEK', 'Swedish krone'), ('RUB', 'Russian ruble')], default='EUR', max_length=5),
        ),
    ]