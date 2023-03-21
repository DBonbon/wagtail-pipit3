# Generated by Django 4.1.7 on 2023-03-20 16:14

from django.db import migrations
import main.blocks.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_productlistpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardspage",
            name="cards",
            field=wagtail.fields.StreamField(
                [
                    (
                        "card",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    main.blocks.blocks.APIImageChooserBlock(
                                        blank=True,
                                        label="image",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "card_title",
                                    wagtail.blocks.CharBlock(label="Card Title"),
                                ),
                                (
                                    "card_subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="another text string can be used as hint, En translation, etc'",
                                        label="Card Subtitle",
                                        required=False,
                                    ),
                                ),
                            ],
                            form_classname="card",
                        ),
                    )
                ],
                use_json_field=True,
            ),
        ),
    ]