# Generated by Django 4.2.4 on 2023-08-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="fooditem",
            name="description",
            field=models.TextField(max_length=200),
        ),
    ]
