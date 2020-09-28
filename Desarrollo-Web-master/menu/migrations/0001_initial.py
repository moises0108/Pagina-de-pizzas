# Generated by Django 3.0.7 on 2020-06-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=999.9)),
                ('type_food', models.CharField(choices=[('0', 'Entradas'), ('1', 'Ensaladas'), ('2', 'Sopas'), ('3', 'Pastas'), ('4', 'Pastas artesanales'), ('5', 'Risottos'), ('6', 'Carne y Pescado'), ('7', 'Grill'), ('8', 'Pizzas'), ('9', 'Postres'), ('10', 'Combos')], max_length=25)),
            ],
        ),
    ]
