# Generated by Django 2.2.19 on 2021-04-01 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0026_instructionpretripbus_instructionpretripclassa_instructionpretripclassb_instructionpretripclassc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accidentprobabilityvaluepretripclassb',
            options={'ordering': ('key', 'field_name'), 'verbose_name': 'Accident Probability Value PreTrip Class B', 'verbose_name_plural': 'Accident Probability Value PreTrip Class B'},
        ),
    ]
