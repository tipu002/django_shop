# Generated by Django 2.2.12 on 2020-08-15 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200812_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='compare_at_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='length_unit',
            field=models.CharField(choices=[('in', 'in'), ('cm', 'cm'), ('m', 'm'), ('ft', 'ft')], default='cm', max_length=4),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='weight_unit',
            field=models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('lb', 'lb')], default='kg', max_length=4),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.Product'),
        ),
    ]
