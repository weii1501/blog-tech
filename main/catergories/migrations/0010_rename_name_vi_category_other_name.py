# Generated by Django 4.2.4 on 2023-09-21 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0009_alter_category_name_alter_category_name_vi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_vi',
            new_name='other_name',
        ),
    ]