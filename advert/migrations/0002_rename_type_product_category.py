# Generated by Django 4.1.7 on 2023-03-31 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='category',
        ),
    ]
