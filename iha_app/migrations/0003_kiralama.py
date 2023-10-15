# Generated by Django 4.2.6 on 2023-10-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iha_app", "0002_iha_details"),
    ]

    operations = [
        migrations.CreateModel(
            name="Kiralama",
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
                ("kullanici_ismi", models.CharField(max_length=100)),
                ("tarih", models.DateField()),
            ],
        ),
    ]
