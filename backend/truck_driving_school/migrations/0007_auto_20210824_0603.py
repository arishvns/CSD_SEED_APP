# Generated by Django 2.2.19 on 2021-08-24 00:03

import django.core.validators
from django.db import migrations, models
import truck_driving_school.models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_driving_school', '0006_trainingrecordcsvtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrecordcsvtemplate',
            name='csv_file',
            field=models.FileField(help_text='File format .csv only', upload_to=truck_driving_school.models.csv_template_file_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
    ]
