# Generated by Django 4.2.7 on 2023-11-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, upload_to='picture'),
        ),
    ]
