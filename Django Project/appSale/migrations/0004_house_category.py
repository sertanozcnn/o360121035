# Generated by Django 4.0 on 2022-11-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSale', '0003_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='House_Category',
            fields=[
                ('House_Category_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('HouseType', models.CharField(max_length=20)),
            ],
        ),
    ]