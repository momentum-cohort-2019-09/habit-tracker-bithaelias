# Generated by Django 2.2.7 on 2019-11-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0011_auto_20191108_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
