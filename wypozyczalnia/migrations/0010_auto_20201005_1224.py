# Generated by Django 3.1.1 on 2020-10-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0009_auto_20201005_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='przedmiot',
            name='dostępnośćPoczątek',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='przedmiot',
            name='dostępnośćZakończenie',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='dataUrodzenia',
            field=models.DateField(),
        ),
    ]
