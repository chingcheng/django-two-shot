# Generated by Django 4.1.3 on 2022-12-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receipt",
            old_name="vender",
            new_name="vendor",
        ),
        migrations.AddField(
            model_name="receipt",
            name="tax",
            field=models.DecimalField(
                decimal_places=3, max_digits=10, null=True
            ),
        ),
    ]