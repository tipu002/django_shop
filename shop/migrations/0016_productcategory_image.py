# Generated by Django 2.2.12 on 2020-08-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_productcategory_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='category/'),
        ),
    ]
