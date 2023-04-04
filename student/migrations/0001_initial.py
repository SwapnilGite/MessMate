# Generated by Django 4.0.3 on 2023-04-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('mis', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=0, max_length=50)),
                ('Year', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=0)),
                ('Dept', models.CharField(default='', max_length=70)),
                ('MessEnrolled', models.CharField(default='', max_length=70)),
                ('pass1', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(default='', max_length=100)),
            ],
        ),
    ]