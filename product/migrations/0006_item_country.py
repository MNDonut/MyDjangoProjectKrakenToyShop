# Generated by Django 3.2.5 on 2021-07-18 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210718_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='country',
            field=models.ForeignKey(default='4', on_delete=django.db.models.deletion.CASCADE, to='product.country'),
        ),
    ]
