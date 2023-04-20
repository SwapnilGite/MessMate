
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messadmin', '0015_bill_total_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealrecord',
            name='mealcount',
            field=models.IntegerField(default=1),
        ),
    ]
