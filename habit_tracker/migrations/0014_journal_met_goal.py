# Generated by Django 2.2.7 on 2019-11-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0013_auto_20191108_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='met_goal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]