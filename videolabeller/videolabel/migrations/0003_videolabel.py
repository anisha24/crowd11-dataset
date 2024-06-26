# Generated by Django 4.2.4 on 2024-05-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videolabel", "0002_rename_new_name_video_label_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                ("last_used", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-last_used"],
            },
        ),
    ]
