from django.db import models

class Academiciens(models.Model):
    id_academicien = models.AutoField(primary_key=True)
    toto = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'academiciens'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()
    

    class Meta:
        managed = True
        db_table = 'migrations'


class Module(models.Model):
    id_module = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    statut = models.IntegerField()
    id_projet = models.ForeignKey('Projet', models.DO_NOTHING, db_column='id_projet')

    class Meta:
        managed = True
        db_table = 'module'


class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date_debut = models.DateField()
    date_fin = models.DateField()
    id_academicien = models.ForeignKey(Academiciens, models.DO_NOTHING, db_column='id_academicien')

    class Meta:
        managed = True
        db_table = 'projet'
