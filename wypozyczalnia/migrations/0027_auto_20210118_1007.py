# Generated by Django 3.1.1 on 2021-01-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0026_auto_20210116_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinia',
            name='wypozyczenia',
        ),
        migrations.AddField(
            model_name='opinia',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
