# Generated by Django 4.0.5 on 2022-06-03 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adocao",
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
                ("valor", models.DecimalField(decimal_places=2, max_digits=5)),
                ("email", models.EmailField(max_length=255)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pet.pet"
                    ),
                ),
            ],
        ),
    ]
