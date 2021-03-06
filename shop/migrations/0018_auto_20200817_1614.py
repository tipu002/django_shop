# Generated by Django 2.2.12 on 2020-08-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_homepagebannerslider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagebannerslider',
            options={'ordering': ('-created',), 'verbose_name': 'Homepage Slider', 'verbose_name_plural': 'Homepage Sliders'},
        ),
        migrations.AlterField(
            model_name='homepagebannerslider',
            name='heading',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='homepagebannerslider',
            name='image',
            field=models.ImageField(default=None, upload_to='homepage/slider/'),
        ),
        migrations.AlterField(
            model_name='homepagebannerslider',
            name='sub_heading',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
