# Generated by Django 4.0.3 on 2023-04-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messadmin', '0004_remove_menu_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Lunch',
        ),
        migrations.AddField(
            model_name='menu',
            name='NonVegDinner',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='menu',
            name='NonVegLunch',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='menu',
            name='VegLunch',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Dinner',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
