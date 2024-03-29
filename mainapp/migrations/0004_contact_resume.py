# Generated by Django 5.0.1 on 2024-02-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_clientreview_client_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('phone_number', models.TextField(blank=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_file', models.FileField(upload_to='resumes')),
            ],
        ),
    ]
