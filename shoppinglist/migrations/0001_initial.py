# Generated by Django 4.1.7 on 2024-10-25 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shop",
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
                ("name", models.CharField(max_length=100)),
                ("shop_site", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=100)),
                ("item_url", models.URLField(blank=True, null=True)),
                ("count", models.PositiveIntegerField(default=0)),
                ("buy_date", models.DateField(blank=True, null=True)),
                ("buy", models.BooleanField(default=False)),
                (
                    "shop",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shoppinglist.shop",
                        verbose_name="shop",
                    ),
                ),
            ],
        ),
    ]
