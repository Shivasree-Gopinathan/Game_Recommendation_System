# Generated by Django 4.2.10 on 2024-03-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="card_last_four",
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]