# Generated by Django 2.2.7 on 2019-11-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0012_auto_20191108_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
