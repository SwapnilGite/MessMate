# Generated by Django 4.0.3 on 2023-04-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messadmin', '0008_remove_mealrecord_bill_paid_alter_mealrecord_meal_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Messname',
            new_name='Mess',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Dinner',
            new_name='VegDinner',
        ),
    ]