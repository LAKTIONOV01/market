# Generated by Django 5.1.5 on 2025-01-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Скидка в %'),
        ),
    ]
