# Generated by Django 4.0.3 on 2023-04-07 12:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_merge_20230407_1821'),
        ('administrator', '0001_initial'),
        ('messadmin', '0005_remove_menu_lunch_menu_nonvegdinner_menu_nonveglunch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='MealRecord',
            fields=[
                ('Meal_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('mealcount', models.IntegerField(default=0)),
                ('Messname', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administrator.mess')),
                ('Student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]