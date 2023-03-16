# Generated by Django 4.1.7 on 2023-03-16 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customimage", "0002_initial"),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="If you want to override the image used on Facebook for",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="customimage.customimage",
            ),
        ),
    ]
