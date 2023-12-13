# Generated by Django 5.0 on 2023-12-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("cpf", models.CharField(max_length=11, verbose_name="cpf")),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="Email"),
                ),
            ],
        ),
    ]
