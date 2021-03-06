# Generated by Django 4.0.2 on 2022-02-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academiciens',
            fields=[
                ('id_academicien', models.AutoField(primary_key=True, serialize=False)),
                ('toto', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'academiciens',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Migrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('migration', models.CharField(max_length=255)),
                ('batch', models.IntegerField()),
            ],
            options={
                'db_table': 'migrations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id_projet', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('id_academicien', models.ForeignKey(db_column='id_academicien', on_delete=django.db.models.deletion.DO_NOTHING, to='projet_api.academiciens')),
            ],
            options={
                'db_table': 'projet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id_module', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('statut', models.IntegerField()),
                ('id_projet', models.ForeignKey(db_column='id_projet', on_delete=django.db.models.deletion.DO_NOTHING, to='projet_api.projet')),
            ],
            options={
                'db_table': 'module',
                'managed': True,
            },
        ),
    ]
