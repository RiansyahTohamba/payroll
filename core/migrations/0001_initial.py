# Generated by Django 4.0 on 2021-12-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city_id', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amnt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('funded_amnt_inv', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
