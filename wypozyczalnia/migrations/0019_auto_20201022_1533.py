# Generated by Django 3.1.1 on 2020-10-22 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0018_auto_20201022_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='przedmiot',
            old_name='zdjęcie',
            new_name='zdjecie',
        ),
    ]
