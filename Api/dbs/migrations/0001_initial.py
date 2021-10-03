# Generated by Django 3.2.7 on 2021-10-03 13:40

import dbs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=dbs.models.nameFile)),
                ('location', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
    ]
