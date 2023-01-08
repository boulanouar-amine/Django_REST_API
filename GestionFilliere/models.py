from django.db import models


class Appartenir(models.Model):
    codeclasse = models.OneToOneField('Classe', models.DO_NOTHING, db_column='CODECLASSE', primary_key=True)  # Field name made lowercase.
    numinscription = models.ForeignKey('Etudiant', models.DO_NOTHING, db_column='NUMINSCRIPTION')  # Field name made lowercase.

    class Meta:

        db_table = 'APPARTENIR'


class Assurer(models.Model):
    codeelmodule = models.OneToOneField('Elementmodule', models.DO_NOTHING, db_column='CODEELMODULE', primary_key=True)  # Field name made lowercase.
    codeenseignant = models.ForeignKey('Enseignant', models.DO_NOTHING, db_column='CODEENSEIGNANT')  # Field name made lowercase.
    typecours = models.ForeignKey('Naturecours', models.DO_NOTHING, db_column='TYPECOURS')  # Field name made lowercase.
    codeclasse = models.ForeignKey('Classe', models.DO_NOTHING, db_column='CODECLASSE')  # Field name made lowercase.
    vhglobal = models.TextField(db_column='VHGLOBAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'ASSURER'


class Classe(models.Model):
    codeclasse = models.AutoField(db_column='CODECLASSE', primary_key=True)  # Field name made lowercase.
    natureclasse = models.TextField(db_column='NATURECLASSE', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'CLASSE'


class Departement(models.Model):
    codedept = models.AutoField(db_column='CODEDEPT', primary_key=True)  # Field name made lowercase.
    codeenseignant = models.ForeignKey('Enseignant', models.DO_NOTHING, db_column='CODEENSEIGNANT',related_name="dep_ens_codeenseignant")  # Field name made lowercase.
    libelledept = models.TextField(db_column='LIBELLEDEPT', blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateField(db_column='DATECREATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'DEPARTEMENT'


class Elementmodule(models.Model):
    codeelmodule = models.AutoField(db_column='CODEELMODULE', primary_key=True)  # Field name made lowercase.
    codemodule = models.ForeignKey('Module', models.DO_NOTHING, db_column='CODEMODULE')  # Field name made lowercase.
    libelleelmodule = models.TextField(db_column='LIBELLEELMODULE', blank=True, null=True)  # Field name made lowercase.
    coefficient = models.IntegerField(db_column='COEFFICIENT', blank=True, null=True)  # Field name made lowercase.
    vh_cm = models.IntegerField(db_column='VH_CM', blank=True, null=True)  # Field name made lowercase.
    vh_td = models.IntegerField(db_column='VH_TD', blank=True, null=True)  # Field name made lowercase.
    vh_tp = models.IntegerField(db_column='VH_TP', blank=True, null=True)  # Field name made lowercase.
    vh_ec = models.IntegerField(db_column='VH_EC', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'ELEMENTMODULE'


class Enseignant(models.Model):
    codeenseignant = models.AutoField(db_column='CODEENSEIGNANT', primary_key=True)  # Field name made lowercase.
    codefiliere = models.ForeignKey('Filiere', models.DO_NOTHING, db_column='CODEFILIERE',related_name='ens_fil_codefiliere')  # Field name made lowercase.
    codedept = models.ForeignKey(Departement, models.DO_NOTHING, db_column='CODEDEPT',related_name='ens_dep_codedept')  # Field name made lowercase.
    nomenseignant = models.TextField(db_column='NOMENSEIGNANT', blank=True, null=True)  # Field name made lowercase.
    prenomenseignant = models.TextField(db_column='PRENOMENSEIGNANT', blank=True, null=True)  # Field name made lowercase.
    tel = models.TextField(db_column='TEL', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:

        db_table = 'ENSEIGNANT'


class Estinscrit(models.Model):
    numinscription = models.OneToOneField('Etudiant', models.DO_NOTHING, db_column='NUMINSCRIPTION', primary_key=True)  # Field name made lowercase.
    codeelmodule = models.ForeignKey(Elementmodule, models.DO_NOTHING, db_column='CODEELMODULE')  # Field name made lowercase.

    class Meta:

        db_table = 'ESTINSCRIT'


class Etudiant(models.Model):
    numinscription = models.AutoField(db_column='NUMINSCRIPTION', primary_key=True)  # Field name made lowercase.
    nometudiant = models.TextField(db_column='NOMETUDIANT', blank=True, null=True)  # Field name made lowercase.
    prenometudiant = models.TextField(db_column='PRENOMETUDIANT', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'ETUDIANT'


class Filiere(models.Model):
    codefiliere = models.AutoField(db_column='CODEFILIERE', primary_key=True)  # Field name made lowercase.
    codedept = models.ForeignKey(Departement, models.DO_NOTHING, db_column='CODEDEPT',related_name='fil_dep_codedept')  # Field name made lowercase.
    codeenseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='CODEENSEIGNANT',related_name='fil_ens_codeenseignant')  # Field name made lowercase.
    intitulefiliere = models.TextField(db_column='INTITULEFILIERE')  # Field name made lowercase.
    dateaccreditation = models.DateField(db_column='DATEACCREDITATION', blank=True, null=True)  # Field name made lowercase.
    dureeaccreditation = models.TextField(db_column='DUREEACCREDITATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'FILIERE'


class Infosuretudiant(models.Model):
    numinscription = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='NUMINSCRIPTION',related_name='inf_etu_numinscription')  # Field name made lowercase.
    datenaissance = models.DateField(db_column='DATENAISSANCE', blank=True, null=True)  # Field name made lowercase.
    dateobtentionbac = models.DateField(db_column='DATEOBTENTIONBAC', blank=True, null=True)  # Field name made lowercase.
    typebac = models.TextField(db_column='TYPEBAC', blank=True, null=True)  # Field name made lowercase.
    mention = models.TextField(db_column='MENTION', blank=True, null=True)  # Field name made lowercase.
    lycee = models.TextField(db_column='LYCEE', blank=True, null=True)  # Field name made lowercase.
    academie = models.TextField(db_column='ACADEMIE', blank=True, null=True)  # Field name made lowercase.
    telephonemobile = models.TextField(db_column='TELEPHONEMOBILE', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    villenaissance = models.TextField(db_column='VILLENAISSANCE', blank=True, null=True)  # Field name made lowercase.
    villeresidence = models.TextField(db_column='VILLERESIDENCE', blank=True, null=True)  # Field name made lowercase.
    adresse = models.TextField(db_column='ADRESSE', blank=True, null=True)  # Field name made lowercase.
    codepostal = models.IntegerField(db_column='CODEPOSTAL', blank=True, null=True)  # Field name made lowercase.
    nationalite = models.TextField(db_column='NATIONALITE', blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:

        db_table = 'INFOSURETUDIANT'


class Module(models.Model):
    codemodule = models.AutoField(db_column='CODEMODULE', primary_key=True)  # Field name made lowercase.
    codefiliere = models.ForeignKey(Filiere, models.DO_NOTHING, db_column='CODEFILIERE')  # Field name made lowercase.
    idsemestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='IDSEMESTRE')  # Field name made lowercase.
    codeenseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='CODEENSEIGNANT')  # Field name made lowercase.
    libellemodule = models.TextField(db_column='LIBELLEMODULE', blank=True, null=True)  # Field name made lowercase.
    naturemodule = models.TextField(db_column='NATUREMODULE', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'MODULE'


class Naturecours(models.Model):
    typecours = models.TextField(db_column='TYPECOURS', primary_key=True)  # Field name made lowercase.
    nbetudiantmax = models.IntegerField(db_column='NBETUDIANTMAX', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'NATURECOURS'


class Obtenir(models.Model):
    codeelmodule = models.OneToOneField(Elementmodule, models.DO_NOTHING, db_column='CODEELMODULE', primary_key=True)  # Field name made lowercase.
    numsession = models.ForeignKey('Session', models.DO_NOTHING, db_column='NUMSESSION')  # Field name made lowercase.
    numinscription = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='NUMINSCRIPTION')  # Field name made lowercase.
    note = models.IntegerField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'OBTENIR'


class Reservation(models.Model):
    datehoraire = models.DateField(db_column='DATEHORAIRE', primary_key=True)  # Field name made lowercase.
    heuredebut = models.TimeField(db_column='HEUREDEBUT')  # Field name made lowercase.
    codeenseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='CODEENSEIGNANT')  # Field name made lowercase.
    typecours = models.ForeignKey(Naturecours, models.DO_NOTHING, db_column='TYPECOURS')  # Field name made lowercase.
    codeelmodule = models.ForeignKey(Elementmodule, models.DO_NOTHING, db_column='CODEELMODULE')  # Field name made lowercase.
    idsalle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='IDSALLE')  # Field name made lowercase.
    heurefin = models.TimeField(db_column='HEUREFIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'RESERVATION'


class Salle(models.Model):
    idsalle = models.AutoField(db_column='IDSALLE', primary_key=True)  # Field name made lowercase.
    capacite = models.IntegerField(db_column='CAPACITE', blank=True, null=True)  # Field name made lowercase.
    typeutilisation = models.TextField(db_column='TYPEUTILISATION', blank=True, null=True)  # Field name made lowercase.
    batiment = models.TextField(db_column='BATIMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'SALLE'


class Semaines(models.Model):
    numsemaine = models.AutoField(db_column='NUMSEMAINE', primary_key=True)  # Field name made lowercase.
    naturesemaine = models.TextField(db_column='NATURESEMAINE', blank=True, null=True)  # Field name made lowercase.
    datelundi = models.DateField(db_column='DATELUNDI', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'SEMAINES'


class Semestre(models.Model):
    idsemestre = models.AutoField(db_column='IDSEMESTRE', primary_key=True)  # Field name made lowercase.
    libellesemestre = models.TextField(db_column='LIBELLESEMESTRE', blank=True, null=True)  # Field name made lowercase.
    niveau = models.TextField(db_column='NIVEAU', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'SEMESTRE'


class Session(models.Model):
    numsession = models.AutoField(db_column='NUMSESSION', primary_key=True)  # Field name made lowercase.
    libellesession = models.TextField(db_column='LIBELLESESSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'SESSION'


class SeProduire(models.Model):
    codefiliere = models.OneToOneField(Filiere, models.DO_NOTHING, db_column='CODEFILIERE', primary_key=True)  # Field name made lowercase.
    idtypeevenement = models.ForeignKey('Typeevenement', models.DO_NOTHING, db_column='IDTYPEEVENEMENT')  # Field name made lowercase.
    idsemestre = models.ForeignKey(Semestre, models.DO_NOTHING, db_column='IDSEMESTRE')  # Field name made lowercase.
    numsemaine = models.ForeignKey(Semaines, models.DO_NOTHING, db_column='NUMSEMAINE')  # Field name made lowercase.
    dateevt = models.DateField(db_column='DATEEVT', blank=True, null=True)  # Field name made lowercase.
    dureeevt = models.TextField(db_column='DUREEEVT', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'SE_PRODUIRE'


class Suivre(models.Model):
    datehoraire = models.OneToOneField(Reservation, models.DO_NOTHING, db_column='DATEHORAIRE', primary_key=True)  # Field name made lowercase.
    heuredebut = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='HEUREDEBUT',related_name='sui_res_heuredebut')  # Field name made lowercase.
    codeclasse = models.ForeignKey(Classe, models.DO_NOTHING, db_column='CODECLASSE',related_name='sui_res_codeclasse')  # Field name made lowercase.

    class Meta:

        db_table = 'SUIVRE'


class SAbsenter(models.Model):
    datehoraire = models.OneToOneField(Reservation, models.DO_NOTHING, db_column='DATEHORAIRE', primary_key=True)  # Field name made lowercase.
    heuredebut = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='HEUREDEBUT',related_name='sab_res_heuredebut')  # Field name made lowercase.
    numinscription = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='NUMINSCRIPTION',related_name='sab_etu_numinscription')  # Field name made lowercase.

    class Meta:

        db_table = 'S_ABSENTER'


class Typeevenement(models.Model):
    idtypeevenement = models.AutoField(db_column='IDTYPEEVENEMENT', primary_key=True)  # Field name made lowercase.
    natureevenement = models.TextField(db_column='NATUREEVENEMENT', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TYPEEVENEMENT'

