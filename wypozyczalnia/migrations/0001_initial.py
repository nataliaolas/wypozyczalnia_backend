# Generated by Django 3.1.1 on 2020-09-07 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DziałPrzedmiotu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zdjęcie', models.ImageField(upload_to='')),
                ('nazwa', models.CharField(max_length=30)),
                ('miasto', models.CharField(max_length=30)),
                ('opisPrzedmiotu', models.TextField()),
                ('dostępnośćPoczątek', models.DateField()),
                ('dostępnośćZakończenie', models.DateField()),
                ('status', models.BooleanField()),
                ('działPrzedmiotu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.działprzedmiotu')),
            ],
        ),
        migrations.CreateModel(
            name='Użytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
                ('hasło', models.CharField(max_length=15)),
                ('miasto', models.CharField(max_length=30)),
                ('dataUrodzenia', models.DateField()),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Wypożyczenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dostępnośćPoczątek', models.DateField()),
                ('dostępnośćZakończenie', models.DateField()),
                ('przedmiot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.przedmiot')),
                ('użytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.użytkownik')),
            ],
        ),
        migrations.AddField(
            model_name='przedmiot',
            name='użytkownikUdostępniający',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.użytkownik'),
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinia', models.TextField()),
                ('skalaZadowolenia', models.IntegerField()),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.użytkownik')),
            ],
        ),
    ]
