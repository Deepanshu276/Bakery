# Generated by Django 3.2.3 on 2021-05-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakery',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
