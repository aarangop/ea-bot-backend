# Generated by Django 4.1.7 on 2023-03-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("permalink", models.CharField(max_length=500)),
                (
                    "hit_or_miss",
                    models.CharField(
                        choices=[("H", "Hit"), ("M", "Miss")], default="H", max_length=2
                    ),
                ),
            ],
        ),
    ]
