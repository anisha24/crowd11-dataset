# Generated by Django 4.1 on 2024-05-21 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videolabel', '0006_alter_label_options_remove_video_new_label_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'ordering': ['-last_used']},
        ),
        migrations.AddField(
            model_name='label',
            name='last_used',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]