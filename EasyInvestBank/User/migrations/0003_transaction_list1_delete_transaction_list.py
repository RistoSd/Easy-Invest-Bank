# Generated by Django 4.0.6 on 2022-09-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_transaction_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_List1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('receiver_IBAN', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction_List',
        ),
    ]