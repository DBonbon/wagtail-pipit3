# Generated by Django 4.1.7 on 2023-03-16 13:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import main.blocks.blocks
import main.mixins
import wagtail.blocks
import wagtail.fields
import wagtail_headless_preview.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("customimage", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BasePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "og_title",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to seo title if empty",
                        max_length=40,
                        null=True,
                        verbose_name="Facebook title",
                    ),
                ),
                (
                    "og_description",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to seo description if empty",
                        max_length=300,
                        null=True,
                        verbose_name="Facebook description",
                    ),
                ),
                (
                    "twitter_title",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to facebook title if empty",
                        max_length=40,
                        null=True,
                        verbose_name="Twitter title",
                    ),
                ),
                (
                    "twitter_description",
                    models.CharField(
                        blank=True,
                        help_text="Fallbacks to facebook description if empty",
                        max_length=300,
                        null=True,
                        verbose_name="Twitter description",
                    ),
                ),
                (
                    "robot_noindex",
                    models.BooleanField(
                        default=False,
                        help_text="Check to add noindex to robots",
                        verbose_name="No index",
                    ),
                ),
                (
                    "robot_nofollow",
                    models.BooleanField(
                        default=False,
                        help_text="Check to add nofollow to robots",
                        verbose_name="No follow",
                    ),
                ),
                (
                    "canonical_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Canonical link"
                    ),
                ),
                (
                    "og_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="If you want to override the image used on Facebook for                     this item, upload an image here.                     The recommended image size for Facebook is 1200 × 630px",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                    ),
                ),
                (
                    "twitter_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Fallbacks to facebook image if empty",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                        verbose_name="Twitter image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(main.mixins.EnhancedEditHandlerMixin, "wagtailcore.page"),
        ),
        migrations.CreateModel(
            name="CardsPage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "intro",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="Describe the cars group's linguistic theme",
                        verbose_name="Intro",
                    ),
                ),
                (
                    "cards",
                    wagtail.fields.StreamField(
                        [
                            (
                                "card",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            main.blocks.blocks.CustomImageChooserBlock(
                                                blank=True,
                                                label="image",
                                                null=True,
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "card_title",
                                            wagtail.blocks.CharBlock(
                                                label="Card Title"
                                            ),
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
                ("card_title", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "card_subtitle",
                    models.CharField(
                        blank=True,
                        help_text="another text string can be used as hint, En translation, etc'",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("min_recommended_age", models.IntegerField(blank=True, null=True)),
                ("max_recommended_age", models.IntegerField(blank=True, null=True)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("af", "Afrikaans"),
                            ("ar", "Arabic"),
                            ("ar-dz", "Algerian Arabic"),
                            ("ast", "Asturian"),
                            ("az", "Azerbaijani"),
                            ("bg", "Bulgarian"),
                            ("be", "Belarusian"),
                            ("bn", "Bengali"),
                            ("br", "Breton"),
                            ("bs", "Bosnian"),
                            ("ca", "Catalan"),
                            ("cs", "Czech"),
                            ("cy", "Welsh"),
                            ("da", "Danish"),
                            ("de", "German"),
                            ("dsb", "Lower Sorbian"),
                            ("el", "Greek"),
                            ("en", "English"),
                            ("en-au", "Australian English"),
                            ("en-gb", "British English"),
                            ("eo", "Esperanto"),
                            ("es", "Spanish"),
                            ("es-ar", "Argentinian Spanish"),
                            ("es-co", "Colombian Spanish"),
                            ("es-mx", "Mexican Spanish"),
                            ("es-ni", "Nicaraguan Spanish"),
                            ("es-ve", "Venezuelan Spanish"),
                            ("et", "Estonian"),
                            ("eu", "Basque"),
                            ("fa", "Persian"),
                            ("fi", "Finnish"),
                            ("fr", "French"),
                            ("fy", "Frisian"),
                            ("ga", "Irish"),
                            ("gd", "Scottish Gaelic"),
                            ("gl", "Galician"),
                            ("he", "Hebrew"),
                            ("hi", "Hindi"),
                            ("hr", "Croatian"),
                            ("hsb", "Upper Sorbian"),
                            ("hu", "Hungarian"),
                            ("hy", "Armenian"),
                            ("ia", "Interlingua"),
                            ("id", "Indonesian"),
                            ("ig", "Igbo"),
                            ("io", "Ido"),
                            ("is", "Icelandic"),
                            ("it", "Italian"),
                            ("ja", "Japanese"),
                            ("ka", "Georgian"),
                            ("kab", "Kabyle"),
                            ("kk", "Kazakh"),
                            ("km", "Khmer"),
                            ("kn", "Kannada"),
                            ("ko", "Korean"),
                            ("ky", "Kyrgyz"),
                            ("lb", "Luxembourgish"),
                            ("lt", "Lithuanian"),
                            ("lv", "Latvian"),
                            ("mk", "Macedonian"),
                            ("ml", "Malayalam"),
                            ("mn", "Mongolian"),
                            ("mr", "Marathi"),
                            ("ms", "Malay"),
                            ("my", "Burmese"),
                            ("nb", "Norwegian Bokmål"),
                            ("ne", "Nepali"),
                            ("nl", "Dutch"),
                            ("nn", "Norwegian Nynorsk"),
                            ("os", "Ossetic"),
                            ("pa", "Punjabi"),
                            ("pl", "Polish"),
                            ("pt", "Portuguese"),
                            ("pt-br", "Brazilian Portuguese"),
                            ("ro", "Romanian"),
                            ("ru", "Russian"),
                            ("sk", "Slovak"),
                            ("sl", "Slovenian"),
                            ("sq", "Albanian"),
                            ("sr", "Serbian"),
                            ("sr-latn", "Serbian Latin"),
                            ("sv", "Swedish"),
                            ("sw", "Swahili"),
                            ("ta", "Tamil"),
                            ("te", "Telugu"),
                            ("tg", "Tajik"),
                            ("th", "Thai"),
                            ("tk", "Turkmen"),
                            ("tr", "Turkish"),
                            ("tt", "Tatar"),
                            ("udm", "Udmurt"),
                            ("uk", "Ukrainian"),
                            ("ur", "Urdu"),
                            ("uz", "Uzbek"),
                            ("vi", "Vietnamese"),
                            ("zh-hans", "Simplified Chinese"),
                            ("zh-hant", "Traditional Chinese"),
                        ],
                        default="en-us",
                        max_length=10,
                    ),
                ),
                (
                    "post_date",
                    models.DateTimeField(
                        default=datetime.datetime.today, verbose_name="Game date"
                    ),
                ),
            ],
            options={
                "verbose_name": "Cards",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Home",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
        migrations.CreateModel(
            name="ArticlePage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "rich_text",
                    wagtail.fields.RichTextField(
                        blank=True, null=True, verbose_name="Rich text"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="If you want to override the image used on Facebook for",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
        migrations.CreateModel(
            name="AboutPage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Company name",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="If you want to override the image used on Facebook for",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="customimage.customimage",
                    ),
                ),
            ],
            options={
                "verbose_name": "About",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
    ]
