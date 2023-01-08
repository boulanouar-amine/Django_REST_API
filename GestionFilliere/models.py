from django.db import models


class Departement(models.Model):
    codedept = models.TextField(db_column='CODEDEPT', primary_key=True)
    libelledept = models.TextField(db_column='LIBELLEDEPT', blank=True, null=True)
    datecreation = models.DateField(db_column='DATECREATION', blank=True, null=True)

    codeenseignant = models.ForeignKey('Enseignant', models.DO_NOTHING, db_column='CODERENSEIGNANT',
                                       related_name="dep_ens_codeenseignant", blank=True, null=True)

    class Meta:
        db_table = 'DEPARTEMENT'

    def __str__(self):
        return self.codedept


class Enseignant(models.Model):
    codeenseignant = models.TextField(db_column='CODEENSEIGNANT', primary_key=True)
    nomenseignant = models.TextField(db_column='NOMENSEIGNANT', blank=True, null=True)
    prenomenseignant = models.TextField(db_column='PRENOMENSEIGNANT', blank=True, null=True)
    tel = models.TextField(db_column='TEL', blank=True, null=True)
    email = models.TextField(db_column='EMAIL', blank=True, null=True)
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)

    class Meta:
        db_table = 'ENSEIGNANT'

    def __str__(self):
        return self.codeenseignant

class Filiere(models.Model):
    codefiliere = models.TextField(db_column='CODEFILIERE', primary_key=True)
    libellefiliere = models.TextField(db_column='LIBELLEFILIERE', blank=True, null=True)
    dateaccreditation = models.DateField(db_column='DATEACCREDITATION', blank=True, null=True)
    dureeaccreditation = models.TextField(db_column='DUREEACCREDITATION', blank=True, null=True)

    codedept = models.ForeignKey(Departement, models.CASCADE, db_column='CODEDEPT',
                                 related_name='fil_dep_codedept', blank=True, null=True)

    codeenseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='CODEENSEIGNANT',
                                       related_name='fil_ens_codeenseignant', blank=True, null=True)

    class Meta:
        db_table = 'FILIERE'

    def __str__(self):
        return self.codefiliere

class Etudiant(models.Model):
    numinscription = models.TextField(db_column='NUMINSCRIPTION', primary_key=True)
    nometudiant = models.TextField(db_column='NOMETUDIANT', blank=True, null=True)
    prenometudiant = models.TextField(db_column='PRENOMETUDIANT', blank=True, null=True)

    class Meta:
        db_table = 'ETUDIANT'


class Semestre(models.Model):
    idsemestre = models.TextField(db_column='IDSEMESTRE', primary_key=True)
    libellesemestre = models.TextField(db_column='LIBELLESEMESTRE', blank=True, null=True)
    niveau = models.TextField(db_column='NIVEAU', blank=True, null=True)

    class Meta:
        db_table = 'SEMESTRE'

    def __str__(self):
        return self.idsemestre


class Module(models.Model):
    codefiliere = models.ForeignKey(Filiere, models.CASCADE, db_column='CODEFILIERE', blank=True, null=True)
    codemodule = models.TextField(db_column='CODEMODULE')
    libellemodule = models.TextField(db_column='LIBELLEMODULE', blank=True, null=True)
    naturemodule = models.TextField(db_column='NATUREMODULE', blank=True, null=True)
    idsemestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='IDSEMESTRE', blank=True, null=True)
    codeenseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='CODEENSEIGNANT', blank=True, null=True)

    class Meta:
        db_table = 'MODULE'
        unique_together = (('codefiliere', 'codemodule'),)

    def __str__(self):
        return self.codemodule


class ElementModule(models.Model):
    codefiliere = models.ForeignKey(Filiere, models.CASCADE, db_column='CODEFILIERE', blank=True, null=True)

    codemodule = models.ForeignKey(Module, models.DO_NOTHING, db_column='CODEMODULE',
                                   related_name="ele_mod_codemodule", blank=True, null=True)
    # code elemet du module
    codeelmodule = models.TextField(db_column='CODEELMODULE')

    libelleelmodule = models.TextField(db_column='LIBELLEELMODULE', blank=True, null=True)
    coefficient = models.FloatField(db_column='COEFFICIENT', blank=True, null=True)
    vh_cm = models.FloatField(db_column='VH_CM', blank=True, null=True)
    vh_td = models.FloatField(db_column='VH_TD', blank=True, null=True)
    vh_tp = models.FloatField(db_column='VH_TP', blank=True, null=True)
    vh_ec = models.FloatField(db_column='VH_EC', blank=True, null=True)

    class Meta:
        db_table = 'ELEMENTMODULE'
        unique_together = (('codefiliere', 'codemodule', 'codeelmodule'),)

    def __str__(self):
        return self.codeelmodule


class Naturecours(models.Model):
    typecours = models.TextField(db_column='TYPECOURS', primary_key=True)
    libellecours = models.TextField(db_column='LIBELLECOURS', blank=True, null=True)
    nbetudiantmax = models.IntegerField(db_column='NBETUDIANTMAX', blank=True, null=True)

    class Meta:
        db_table = 'NATURECOURS'

    def __str__(self):
        return self.typecours

class Classe(models.Model):
    codeclasse = models.TextField(db_column='CODECLASSE', primary_key=True)
    natureclasse = models.TextField(db_column='NATURECLASSE', blank=True, null=True)

    class Meta:
        db_table = 'CLASSE'

    def __str__(self):
        return self.codeclasse


class ClassEtudiant(models.Model):
    codeclass = models.ForeignKey(Classe, models.CASCADE, db_column='CODECLASS', blank=True, null=True)
    numinscription = models.ForeignKey(Etudiant, models.CASCADE, db_column='NUMINSCRIPTION', blank=True, null=True)

    class Meta:
        db_table = 'CLASSEETUDIANT'
        unique_together = (('codeclass', 'numinscription'),)

    def __str__(self):
        return self.codeclass + " " + self.numinscription

class ChargeHoraireEnseignant(models.Model):
    codeenseignant = models.ForeignKey(Enseignant, models.CASCADE, db_column='CODEENSEIGNANT', blank=True, null=True)
    codefiliere = models.ForeignKey(Filiere, models.CASCADE, db_column='CODEFILIERE', blank=True, null=True)
    codemodule = models.ForeignKey(Module, models.CASCADE, db_column='CODEMODULE', blank=True, null=True)
    codeelmodule = models.ForeignKey(ElementModule, models.CASCADE, db_column='CODEELMODULE', blank=True, null=True)
    codeclass = models.ForeignKey(Classe, models.CASCADE, db_column='CODECLASS', blank=True, null=True)
    typecours = models.ForeignKey(Naturecours, models.CASCADE, db_column='TYPECOURS', blank=True, null=True)
    vhglobal = models.FloatField(db_column='VHGLOBAL', blank=True, null=True)


    class Meta:
        db_table = 'CHARGEHORAIREENSEIGNANT'

    def __str__(self):
        return str(self.codeenseignant) + " " + str(self.codefiliere) + " " + str(self.codemodule) + " "\
            + str(self.codeelmodule) + " " + str(self.codeclass) + " " + str(self.typecours)


class Session(models.Model):
    numsession = models.AutoField(db_column='NUMSESSION', primary_key=True)
    libellesession = models.TextField(db_column='LIBELLESESSION', blank=True, null=True)

    class Meta:
        db_table = 'SESSION'

    def __str__(self):
        return self.numsession


class Note(models.Model):
    numinscription = models.ForeignKey(Etudiant, models.CASCADE, db_column='NUMINSCRIPTION', blank=True, null=True)
    codefiliere = models.ForeignKey(Filiere, models.CASCADE, db_column='CODEFILIERE', blank=True, null=True)
    codemodule = models.ForeignKey(Module, models.CASCADE, db_column='CODEMODULE', blank=True, null=True)
    codeelmodule = models.ForeignKey(ElementModule, models.CASCADE, db_column='CODEELMODULE', blank=True, null=True)
    numsession = models.ForeignKey(Session, models.CASCADE, db_column='NUMSESSION', blank=True, null=True)
    note = models.FloatField(db_column='NOTE', blank=True, null=True)


class Infosuretudiant(models.Model):
    numinscription = models.ForeignKey(Etudiant, models.CASCADE, db_column='NUMINSCRIPTION',
                                       related_name='inf_etu_numinscription')

    datenaissance = models.DateField(db_column='DATENAISSANCE', blank=True, null=True)
    dateobtentionbac = models.DateField(db_column='DATEOBTENTIONBAC', blank=True, null=True)

    typebac = models.TextField(db_column='TYPEBAC', blank=True, null=True)
    mention = models.TextField(db_column='MENTION', blank=True, null=True)
    lycee = models.TextField(db_column='LYCEE', blank=True, null=True)
    academie = models.TextField(db_column='ACADEMIE', blank=True, null=True)
    telephonemobile = models.TextField(db_column='TELEPHONEMOBILE', blank=True, null=True)
    email = models.TextField(db_column='EMAIL', blank=True, null=True)
    villenaissance = models.TextField(db_column='VILLENAISSANCE', blank=True, null=True)
    villeresidence = models.TextField(db_column='VILLERESIDENCE', blank=True, null=True)
    adresse = models.TextField(db_column='ADRESSE', blank=True, null=True)
    codepostal = models.IntegerField(db_column='CODEPOSTAL', blank=True, null=True)
    nationalite = models.TextField(db_column='NATIONALITE', blank=True, null=True)
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)

    class Meta:
        db_table = 'INFOSURETUDIANT'


class Reservation(models.Model):
    datehoraire = models.DateField(db_column='DATEHORAIRE', primary_key=True)
    heuredebut = models.TimeField(db_column='HEUREDEBUT')

    codeenseignant = models.ForeignKey(Enseignant, models.CASCADE, db_column='CODEENSEIGNANT')
    typecours = models.ForeignKey(Naturecours, models.DO_NOTHING, db_column='TYPECOURS', blank=True, null=True)
    codeelmodule = models.ForeignKey(ElementModule, models.DO_NOTHING, db_column='CODEELMODULE')
    idsalle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='IDSALLE')

    heurefin = models.TimeField(db_column='HEUREFIN', blank=True, null=True)

    class Meta:
        db_table = 'RESERVATION'


class Salle(models.Model):
    idsalle = models.AutoField(db_column='IDSALLE', primary_key=True)
    capacite = models.IntegerField(db_column='CAPACITE', blank=True, null=True)
    typeutilisation = models.TextField(db_column='TYPEUTILISATION', blank=True, null=True)
    batiment = models.TextField(db_column='BATIMENT', blank=True, null=True)

    class Meta:
        db_table = 'SALLE'


class Semaines(models.Model):
    numsemaine = models.AutoField(db_column='NUMSEMAINE', primary_key=True)
    naturesemaine = models.TextField(db_column='NATURESEMAINE', blank=True, null=True)
    datelundi = models.DateField(db_column='DATELUNDI', blank=True, null=True)

    class Meta:
        db_table = 'SEMAINES'
