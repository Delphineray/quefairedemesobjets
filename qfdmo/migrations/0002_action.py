# Generated by Django 4.2.3 on 2023-08-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qfdmo", "0001_categories_subcategories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("lvao_id", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]