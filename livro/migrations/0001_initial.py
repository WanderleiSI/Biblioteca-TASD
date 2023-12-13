# Generated by Django 5.0 on 2023-12-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Livro",
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
                ("nome", models.CharField(max_length=30, verbose_name="Nome")),
                ("editora", models.CharField(max_length=15, verbose_name="Editora")),
                ("ano", models.DateField(null=True, verbose_name="Ano")),
            ],
        ),
    ]