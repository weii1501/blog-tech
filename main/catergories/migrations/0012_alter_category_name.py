# Generated by Django 4.2.4 on 2023-09-21 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0011_category_icon_alter_category_other_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Chuyên mục'),
        ),
    ]
