# Generated by Django 4.1.5 on 2023-03-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_blogmodel_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogmodel",
            old_name="titel",
            new_name="title",
        ),
    ]