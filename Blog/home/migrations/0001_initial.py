# Generated by Django 4.1.5 on 2023-03-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogModel",
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
                ("titel", models.CharField(max_length=500)),
                ("content", models.TextField()),
                ("slug", models.SlugField(max_length=100)),
                ("image", models.ImageField(upload_to="blog")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("upload_to", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
