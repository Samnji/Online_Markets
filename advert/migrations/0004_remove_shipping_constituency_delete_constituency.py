# Generated by Django 4.1.7 on 2023-04-03 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='constituency',
        ),
        migrations.DeleteModel(
            name='Constituency',
        ),
    ]
