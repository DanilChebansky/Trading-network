# Generated by Django 4.2.2 on 2024-12-07 14:49

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="почта",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="страна"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="улица"
                    ),
                ),
                (
                    "home",
                    models.CharField(
                        blank=True, max_length=25, null=True, verbose_name="дом"
                    ),
                ),
            ],
            options={
                "verbose_name": "контакты",
                "verbose_name_plural": "контакты",
            },
        ),
        migrations.CreateModel(
            name="Network",
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
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("factory", "завод"),
                            ("network", "розничная сеть"),
                            ("IP", "ИП"),
                        ],
                        max_length=150,
                        verbose_name="название звена сети",
                    ),
                ),
                (
                    "arrears",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=50,
                        null=True,
                        verbose_name="задолженность",
                    ),
                ),
                (
                    "creation_time",
                    models.TimeField(
                        auto_now_add=True, null=True, verbose_name="время создания"
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "contacts",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.contacts",
                        verbose_name="контакты",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="products.product",
                        verbose_name="продукты",
                    ),
                ),
                (
                    "supplier",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="network.network",
                        verbose_name="поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "сеть",
                "verbose_name_plural": "сеть",
            },
        ),
    ]