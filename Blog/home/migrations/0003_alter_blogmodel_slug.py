# Generated by Django 4.1.5 on 2023-03-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_blogmodel_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogmodel",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]