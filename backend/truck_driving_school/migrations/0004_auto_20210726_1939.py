# Generated by Django 2.2.19 on 2021-07-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_driving_school', '0003_drivertrainigrecord_traininglocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininglocation',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Location Name'),
        ),
    ]
