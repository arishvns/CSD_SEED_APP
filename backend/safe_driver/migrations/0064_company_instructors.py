# Generated by Django 2.2.24 on 2021-10-15 07:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('safe_driver', '0063_auto_20211015_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='instructors',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
