# Generated by Django 4.2.1 on 2024-01-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prompt_studio_core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customtool",
            name="output",
            field=models.TextField(
                blank=True, db_comment="Field to store the output format type."
            ),
        ),
    ]
