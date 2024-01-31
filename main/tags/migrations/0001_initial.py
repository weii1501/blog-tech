# Generated by Django 4.2.3 on 2023-08-09 09:13

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=True, max_length=100, populate_from='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
