# Generated by Django 3.2.5 on 2021-07-18 16:23

from django.db import migrations, models
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_item_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='country',
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='item',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=slugger.fields.AutoSlugField(default='', populate_from='title'),
        ),
    ]