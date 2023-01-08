-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql

PRAGMA journal_mode = MEMORY;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;


create table APPARTENIR
(
CODECLASSE           int not null,
NUMINSCRIPTION       int not null,

primary key (CODECLASSE, NUMINSCRIPTION),

foreign key (NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict,

foreign key (CODECLASSE)
references CLASSE (CODECLASSE) on delete restrict on update restrict

);
create table ASSURER
(
CODEELMODULE         int not null,
CODEENSEIGNANT       int not null,
TYPECOURS            TEXT not null,
CODECLASSE           int not null,
VHGLOBAL             TEXT,
primary key (CODEELMODULE, CODEENSEIGNANT, TYPECOURS, CODECLASSE),

foreign key (CODECLASSE)
references CLASSE (CODECLASSE) on delete restrict on update restrict,

foreign key (CODEELMODULE)
references ELEMENTMODULE (CODEELMODULE) on delete restrict on update restrict,

foreign key (CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (TYPECOURS)
references NATURECOURS (TYPECOURS) on delete restrict on update restrict

);
create table CLASSE
(
CODECLASSE           int not null,
NATURECLASSE         TEXT,
primary key (CODECLASSE)
);
create table DEPARTEMENT
(
CODEDEPT             int not null,
CODEENSEIGNANT       int not null,
ENS_CODEENSEIGNANT   int not null,
LIBELLEDEPT          TEXT,
DATECREATION         date,
primary key (CODEDEPT),

foreign key (ENS_CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict

);
create table ELEMENTMODULE
(
CODEELMODULE         int not null,
CODEMODULE           int not null,
LIBELLEELMODULE      TEXT,
COEFFICIENT          int,
VH_CM                int,
VH_TD                int,
VH_TP                int,
VH_EC                int,
primary key (CODEELMODULE),

foreign key (CODEMODULE)
references MODULE (CODEMODULE) on delete restrict on update restrict
);
create table ENSEIGNANT
(
CODEENSEIGNANT       int not null,
CODEFILIERE          int not null,
FIL_CODEFILIERE      int not null,
CODEDEPT             int not null,
DEP_CODEDEPT         int not null,
DEP_CODEDEPT2        int not null,
NOMENSEIGNANT        TEXT,
PRENOMENSEIGNANT     TEXT,
TEL                  TEXT,
EMAIL                TEXT,
PHOTO                longblob,
primary key (CODEENSEIGNANT),

foreign key (CODEFILIERE)
references FILIERE (CODEFILIERE) on delete restrict on update restrict,

foreign key (FIL_CODEFILIERE)
references FILIERE (CODEFILIERE) on delete restrict on update restrict,

foreign key (DEP_CODEDEPT)
references DEPARTEMENT (CODEDEPT) on delete restrict on update restrict,

foreign key (DEP_CODEDEPT2)
references DEPARTEMENT (CODEDEPT) on delete restrict on update restrict,

foreign key (CODEDEPT)
references DEPARTEMENT (CODEDEPT) on delete restrict on update restrict

);
create table ESTINSCRIT
(
NUMINSCRIPTION       int not null,
CODEELMODULE         int not null,
primary key (NUMINSCRIPTION, CODEELMODULE),

foreign key (CODEELMODULE)
references ELEMENTMODULE (CODEELMODULE) on delete restrict on update restrict,

foreign key (NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict


);
create table ETUDIANT
(
NUMINSCRIPTION       int not null,
NOMETUDIANT          TEXT,
PRENOMETUDIANT       TEXT,
primary key (NUMINSCRIPTION)

-- foreign key (NUMINSCRIPTION)
-- references INFOSURETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict


);
create table FILIERE
(
CODEFILIERE          int not null,
CODEDEPT             int not null,
CODEENSEIGNANT       int not null,
ENS_CODEENSEIGNANT   int not null,
INTITULEFILIERE      TEXT not null,
DATEACCREDITATION    date,
DUREEACCREDITATION   TEXT,
primary key (CODEFILIERE),

foreign key (ENS_CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (CODEDEPT)
references DEPARTEMENT (CODEDEPT) on delete restrict on update restrict

);
create table INFOSURETUDIANT
(
NUMINSCRIPTION       int not null,
ETU_NUMINSCRIPTION   int not null,
DATENAISSANCE        date,
DATEOBTENTIONBAC     date,
TYPEBAC              TEXT,
MENTION              TEXT,
LYCEE                TEXT,
ACADEMIE             TEXT,
TELEPHONEMOBILE      TEXT,
EMAIL                TEXT,
VILLENAISSANCE       TEXT,
VILLERESIDENCE       TEXT,
ADRESSE              TEXT,
CODEPOSTAL           int,
NATIONALITE          TEXT,
PHOTO                longblob,

foreign key (ETU_NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict,

foreign key (NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict

);
create table MODULE
(
CODEMODULE           int not null,
CODEFILIERE          int not null,
IDSEMESTRE           int not null,
CODEENSEIGNANT       int not null,
LIBELLEMODULE        TEXT,
NATUREMODULE         TEXT,
primary key (CODEMODULE),

foreign key (CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (CODEFILIERE)
references FILIERE (CODEFILIERE) on delete restrict on update restrict,

foreign key (IDSEMESTRE)
references SEMESTRE (IDSEMESTRE) on delete restrict on update restrict

);
create table NATURECOURS
(
TYPECOURS            TEXT not null,
NBETUDIANTMAX        int,
primary key (TYPECOURS)
);
create table OBTENIR
(
CODEELMODULE         int not null,
NUMSESSION           int not null,
NUMINSCRIPTION       int not null,
NOTE                 int,
primary key (CODEELMODULE, NUMSESSION, NUMINSCRIPTION),


foreign key (NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict,

foreign key (CODEELMODULE)
references ELEMENTMODULE (CODEELMODULE) on delete restrict on update restrict,

foreign key (NUMSESSION)
references SESSION (NUMSESSION) on delete restrict on update restrict



);
create table RESERVATION
(
DATEHORAIRE          date not null,
HEUREDEBUT           time not null,
CODEENSEIGNANT       int not null,
TYPECOURS            TEXT not null,
CODEELMODULE         int not null,
IDSALLE              int not null,
HEUREFIN             time,
primary key (DATEHORAIRE, HEUREDEBUT),

foreign key (IDSALLE)
references SALLE (IDSALLE) on delete restrict on update restrict,

foreign key (CODEENSEIGNANT)
references ENSEIGNANT (CODEENSEIGNANT) on delete restrict on update restrict,

foreign key (TYPECOURS)
references NATURECOURS (TYPECOURS) on delete restrict on update restrict,

foreign key (CODEELMODULE)
references ELEMENTMODULE (CODEELMODULE) on delete restrict on update restrict

);
create table SALLE
(
IDSALLE              int not null,
CAPACITE             int,
TYPEUTILISATION      TEXT,
BATIMENT             TEXT,
primary key (IDSALLE)
);
create table SEMAINES
(
NUMSEMAINE           int not null,
NATURESEMAINE        TEXT,
DATELUNDI            date,
primary key (NUMSEMAINE)
);
create table SEMESTRE
(
IDSEMESTRE           int not null,
LIBELLESEMESTRE      TEXT,
NIVEAU               TEXT,
primary key (IDSEMESTRE)
);
create table SESSION
(
NUMSESSION           int not null,
LIBELLESESSION       TEXT,
primary key (NUMSESSION)
);
create table SE_PRODUIRE
(
CODEFILIERE          int not null,
IDTYPEEVENEMENT      int not null,
IDSEMESTRE           int not null,
NUMSEMAINE           int not null,
DATEEVT              date,
DUREEEVT             TEXT,
primary key (CODEFILIERE, IDTYPEEVENEMENT, IDSEMESTRE, NUMSEMAINE),

foreign key (NUMSEMAINE)
references SEMAINES (NUMSEMAINE) on delete restrict on update restrict,

foreign key (CODEFILIERE)
references FILIERE (CODEFILIERE) on delete restrict on update restrict,

foreign key (IDTYPEEVENEMENT)
references TYPEEVENEMENT (IDTYPEEVENEMENT) on delete restrict on update restrict,

foreign key (IDSEMESTRE)
references SEMESTRE (IDSEMESTRE) on delete restrict on update restrict


);
create table SUIVRE
(
DATEHORAIRE          date not null,
HEUREDEBUT           time not null,
CODECLASSE           int not null,
primary key (DATEHORAIRE, HEUREDEBUT, CODECLASSE),

foreign key (CODECLASSE)
references CLASSE (CODECLASSE) on delete restrict on update restrict,

foreign key (DATEHORAIRE, HEUREDEBUT)
references RESERVATION (DATEHORAIRE, HEUREDEBUT) on delete restrict on update restrict
);
create table S_ABSENTER
(
DATEHORAIRE          date not null,
HEUREDEBUT           time not null,
NUMINSCRIPTION       int not null,
primary key (DATEHORAIRE, HEUREDEBUT, NUMINSCRIPTION),

foreign key (NUMINSCRIPTION)
references ETUDIANT (NUMINSCRIPTION) on delete restrict on update restrict,

foreign key (DATEHORAIRE, HEUREDEBUT)
references RESERVATION (DATEHORAIRE, HEUREDEBUT) on delete restrict on update restrict
);
create table TYPEEVENEMENT
(
IDTYPEEVENEMENT      int not null,
NATUREEVENEMENT      TEXT,
DESCRIPTION          TEXT,
primary key (IDTYPEEVENEMENT)
);







PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
