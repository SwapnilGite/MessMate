# Generated by Django 4.0.3 on 2023-04-08 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messadmin', '0010_rename_mess_name_messadmin_mess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Brekfast',
            new_name='Breakfast',
        ),
    ]
