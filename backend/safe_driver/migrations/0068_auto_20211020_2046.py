# Generated by Django 2.2.24 on 2021-10-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0067_auto_20211019_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructionbtwbus',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionbtwclassa',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionbtwclassb',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionbtwclassc',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionbtwclassp',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionpretripbus',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionpretripclassa',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionpretripclassb',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionpretripclassc',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionswp',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='instructionvrt',
            name='field_name',
            field=models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=250, verbose_name='Field Name'),
        ),
    ]
