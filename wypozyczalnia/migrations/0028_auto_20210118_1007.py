# Generated by Django 3.1.1 on 2021-01-18 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0027_auto_20210118_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinia',
            name='uzytkownik',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.uzytkownik'),
        ),
    ]
