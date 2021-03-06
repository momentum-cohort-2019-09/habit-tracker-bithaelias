# Generated by Django 2.2.7 on 2019-11-07 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0004_remove_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='habit',
            name='title',
        ),
        migrations.AddField(
            model_name='habit',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='habit',
            field=models.CharField(default='habit', max_length=255),
        ),
        migrations.AddField(
            model_name='habit',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.AddField(
            model_name='journal',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='journal', to='habit_tracker.Habit'),
        ),
    ]
