# Generated by Django 4.0.3 on 2023-04-10 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_merge_0012_alter_student_year_0012_auto_20230408_1415'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
