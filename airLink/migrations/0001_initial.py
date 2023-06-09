# Generated by Django 4.1 on 2023-05-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AirLink",
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
                ("link", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "AirLink",
                "verbose_name_plural": "AirLink",
                "db_table": "air_link",
            },
        ),
    ]
