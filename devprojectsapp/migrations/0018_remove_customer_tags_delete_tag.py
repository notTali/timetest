# Generated by Django 4.0.5 on 2022-07-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetestapp', '0017_remove_tag_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
