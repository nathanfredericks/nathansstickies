# Generated by Django 4.0.5 on 2022-06-12 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stickies', '0004_computer_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sticky',
            name='computer',
        ),
        migrations.AddField(
            model_name='sticky',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Computer',
        ),
    ]
