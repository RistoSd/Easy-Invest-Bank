# Generated by Django 4.0.6 on 2022-09-05 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_transaction_list_receiver_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction_list',
            name='receiver_name',
        ),
    ]
