# Generated by Django 4.0.5 on 2022-07-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetestapp', '0006_alter_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='1.jpeg', null=True, upload_to=''),
        ),
    ]