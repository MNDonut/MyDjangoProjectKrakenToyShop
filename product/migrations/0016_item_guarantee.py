# Generated by Django 3.2.5 on 2021-07-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_guarantee'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='guarantee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, null=True, to='product.guarantee'),
        ),
    ]
