# Generated by Django 2.2.19 on 2021-03-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0020_auto_20210312_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentProbabilityValueBTWClassC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Name')),
                ('key', models.CharField(choices=[('animal', 'Animal'), ('backing', 'Backing'), ('cyclist', 'Cyclist'), ('entering_exiting', 'Entering/Exiting'), ('hazardous_materials', 'Hazardous Materials'), ('head_on_collision', 'Head-on Collision'), ('hit_in_rear', 'Hit in Rear'), ('hit_other_in_rear', 'Hit Other in Rear'), ('hit_parked_vehicle', 'Hit Parked Vehicle'), ('hit_stationary_object', 'Hit Stationary Object'), ('hit_while_parked', 'Hit While Parked'), ('intersection', 'Intersection'), ('jacknife', 'Jacknife'), ('moving_object', 'Moving Object'), ('parking_lot', 'Parking Lot'), ('rollaway', 'Rollaway'), ('sideswipe', 'Sideswipe')], default=None, help_text='Type key name underscore and without any space', max_length=32, verbose_name='Key')),
                ('field_name', models.CharField(default=None, help_text='Type field name underscore and without any space matched with db field', max_length=32, verbose_name='Field')),
                ('value', models.PositiveIntegerField(default=None, help_text='Postive Number Value', verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Accident Probability Value BTW Class C',
                'verbose_name_plural': 'Accident Probability Value BTW Class C',
                'ordering': ('name',),
                'unique_together': {('key', 'field_name')},
            },
        ),
        migrations.CreateModel(
            name='AccidentProbabilityValueBTWClassB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Name')),
                ('key', models.CharField(choices=[('animal', 'Animal'), ('backing', 'Backing'), ('cyclist', 'Cyclist'), ('entering_exiting', 'Entering/Exiting'), ('hazardous_materials', 'Hazardous Materials'), ('head_on_collision', 'Head-on Collision'), ('hit_in_rear', 'Hit in Rear'), ('hit_other_in_rear', 'Hit Other in Rear'), ('hit_parked_vehicle', 'Hit Parked Vehicle'), ('hit_stationary_object', 'Hit Stationary Object'), ('hit_while_parked', 'Hit While Parked'), ('intersection', 'Intersection'), ('jacknife', 'Jacknife'), ('moving_object', 'Moving Object'), ('parking_lot', 'Parking Lot'), ('rollaway', 'Rollaway'), ('sideswipe', 'Sideswipe')], default=None, help_text='Type key name underscore and without any space', max_length=32, verbose_name='Key')),
                ('field_name', models.CharField(default=None, help_text='Type field name underscore and without any space matched with db field', max_length=32, verbose_name='Field')),
                ('value', models.PositiveIntegerField(default=None, help_text='Postive Number Value', verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Accident Probability Value BTW Class B',
                'verbose_name_plural': 'Accident Probability Value BTW Class B',
                'ordering': ('name',),
                'unique_together': {('key', 'field_name')},
            },
        ),
        migrations.CreateModel(
            name='AccidentProbabilityValueBTWClassA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Name')),
                ('key', models.CharField(choices=[('animal', 'Animal'), ('backing', 'Backing'), ('cyclist', 'Cyclist'), ('entering_exiting', 'Entering/Exiting'), ('hazardous_materials', 'Hazardous Materials'), ('head_on_collision', 'Head-on Collision'), ('hit_in_rear', 'Hit in Rear'), ('hit_other_in_rear', 'Hit Other in Rear'), ('hit_parked_vehicle', 'Hit Parked Vehicle'), ('hit_stationary_object', 'Hit Stationary Object'), ('hit_while_parked', 'Hit While Parked'), ('intersection', 'Intersection'), ('jacknife', 'Jacknife'), ('moving_object', 'Moving Object'), ('parking_lot', 'Parking Lot'), ('rollaway', 'Rollaway'), ('sideswipe', 'Sideswipe')], default=None, help_text='Type key name underscore and without any space', max_length=32, verbose_name='Key')),
                ('field_name', models.CharField(default=None, help_text='Type field name underscore and without any space matched with db field', max_length=32, verbose_name='Field')),
                ('value', models.PositiveIntegerField(default=None, help_text='Postive Number Value', verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Accident Probability Value BTW Class A',
                'verbose_name_plural': 'Accident Probability Value BTW Class A',
                'ordering': ('name',),
                'unique_together': {('key', 'field_name')},
            },
        ),
        migrations.CreateModel(
            name='AccidentProbabilityValueBTWBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Name')),
                ('key', models.CharField(choices=[('animal', 'Animal'), ('backing', 'Backing'), ('cyclist', 'Cyclist'), ('entering_exiting', 'Entering/Exiting'), ('hazardous_materials', 'Hazardous Materials'), ('head_on_collision', 'Head-on Collision'), ('hit_in_rear', 'Hit in Rear'), ('hit_other_in_rear', 'Hit Other in Rear'), ('hit_parked_vehicle', 'Hit Parked Vehicle'), ('hit_stationary_object', 'Hit Stationary Object'), ('hit_while_parked', 'Hit While Parked'), ('intersection', 'Intersection'), ('jacknife', 'Jacknife'), ('moving_object', 'Moving Object'), ('parking_lot', 'Parking Lot'), ('rollaway', 'Rollaway'), ('sideswipe', 'Sideswipe')], default=None, help_text='Type key name underscore and without any space', max_length=32, verbose_name='Key')),
                ('field_name', models.CharField(default=None, help_text='Type field name underscore and without any space matched with db field', max_length=32, verbose_name='Field')),
                ('value', models.PositiveIntegerField(default=None, help_text='Postive Number Value', verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Accident Probability Value BTW BUS',
                'verbose_name_plural': 'Accident Probability Value BTW BUS',
                'ordering': ('name',),
                'unique_together': {('key', 'field_name')},
            },
        ),
    ]
