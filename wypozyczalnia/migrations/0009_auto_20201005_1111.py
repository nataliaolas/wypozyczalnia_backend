# Generated by Django 3.1.1 on 2020-10-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0008_auto_20201005_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uzytkownik',
            old_name='numertelefonu',
            new_name='numerTelefonu',
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='dataUrodzenia',
            field=models.DateField(verbose_name='%Y-%m-%d'),
        ),
    ]
