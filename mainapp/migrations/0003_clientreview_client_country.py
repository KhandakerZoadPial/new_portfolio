# Generated by Django 5.0.1 on 2024-02-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_clientreview_client_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientreview',
            name='client_country',
            field=models.TextField(blank=True),
        ),
    ]
