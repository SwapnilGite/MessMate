# Generated by Django 4.0.3 on 2023-04-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_merge_20230407_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]