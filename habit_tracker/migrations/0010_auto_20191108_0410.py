# Generated by Django 2.2.7 on 2019-11-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0009_auto_20191108_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit',
            field=models.CharField(blank=True, choices=[('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], max_length=255, null=True),
        ),
    ]
