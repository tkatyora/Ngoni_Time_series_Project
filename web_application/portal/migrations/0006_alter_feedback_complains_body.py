# Generated by Django 5.0.1 on 2024-01-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0005_alter_feedback_complains_reply_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback_complains",
            name="body",
            field=models.TextField(blank=True, default="None", null=True),
        ),
    ]