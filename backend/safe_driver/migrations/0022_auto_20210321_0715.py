# Generated by Django 2.2.19 on 2021-03-21 01:15

from django.db import migrations, models
import safe_driver.image_functions


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0021_accidentprobabilityvaluebtwbus_accidentprobabilityvaluebtwclassa_accidentprobabilityvaluebtwclassb_a'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accidentprobabilityvaluebtwbus',
            options={'ordering': ('key', 'field_name'), 'verbose_name': 'Accident Probability Value BTW BUS', 'verbose_name_plural': 'Accident Probability Value BTW BUS'},
        ),
        migrations.AlterModelOptions(
            name='accidentprobabilityvaluebtwclassa',
            options={'ordering': ('key', 'field_name'), 'verbose_name': 'Accident Probability Value BTW Class A', 'verbose_name_plural': 'Accident Probability Value BTW Class A'},
        ),
        migrations.AlterModelOptions(
            name='accidentprobabilityvaluebtwclassb',
            options={'ordering': ('key', 'field_name'), 'verbose_name': 'Accident Probability Value BTW Class B', 'verbose_name_plural': 'Accident Probability Value BTW Class B'},
        ),
        migrations.AlterModelOptions(
            name='accidentprobabilityvaluebtwclassc',
            options={'ordering': ('key', 'field_name'), 'verbose_name': 'Accident Probability Value BTW Class C', 'verbose_name_plural': 'Accident Probability Value BTW Class C'},
        ),
        migrations.AddField(
            model_name='btwbus',
            name='map_image',
            field=models.ImageField(blank=True, null=True, upload_to=safe_driver.image_functions.map_image_folder, verbose_name='Map Image'),
        ),
        migrations.AddField(
            model_name='btwclassa',
            name='map_image',
            field=models.ImageField(blank=True, null=True, upload_to=safe_driver.image_functions.map_image_folder, verbose_name='Map Image'),
        ),
        migrations.AddField(
            model_name='btwclassb',
            name='map_image',
            field=models.ImageField(blank=True, null=True, upload_to=safe_driver.image_functions.map_image_folder, verbose_name='Map Image'),
        ),
        migrations.AddField(
            model_name='btwclassc',
            name='map_image',
            field=models.ImageField(blank=True, null=True, upload_to=safe_driver.image_functions.map_image_folder, verbose_name='Map Image'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluebtwclassa',
            name='field_name',
            field=models.CharField(default=None, help_text='Type field name underscore and without any space matched with db field', max_length=32, verbose_name='Field Name'),
        ),
    ]
