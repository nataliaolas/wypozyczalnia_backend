# Generated by Django 3.1.1 on 2021-01-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0031_auto_20210118_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='przedmiot',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to='przedmiot', verbose_name='Image'),
        ),
    ]
