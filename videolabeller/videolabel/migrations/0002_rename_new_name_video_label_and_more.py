# Generated by Django 5.0.4 on 2024-05-03 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videolabel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='new_name',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='original_name',
            new_name='video_name',
        ),
    ]
