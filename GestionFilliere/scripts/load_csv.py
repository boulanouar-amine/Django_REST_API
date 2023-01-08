
from datetime import datetime

from ..models import *
import csv


def run():
    def check_number(value):

        if value == '':
            return None
        else:
            return value

    with open('Import/enseignant.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            enseignant, _ = Enseignant.objects.get_or_create(codeenseignant=row[0], nomenseignant=row[1],
                                                             prenomenseignant=row[2], tel=row[3], email=row[4])
            enseignant.save()


    with open('Import/departement.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Departement.objects.all().delete()

        for row in reader:
            datecreation = datetime.strptime(row[2], '%d/%m/%Y').date()
            enseignant , _ = Enseignant.objects.get_or_create(codeenseignant=row[3])

            departement, _ = Departement.objects.get_or_create(codedept=row[0], libelledept=row[1], datecreation=datecreation,
                                                               codeenseignant=enseignant)

            departement.save()

    with open('Import/filiere.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dateaccreditation = datetime.strptime(row[2], '%d/%m/%Y').date()
            departement, _ = Departement.objects.get_or_create(codedept=row[4])
            enseignant, _ = Enseignant.objects.get_or_create(codeenseignant=row[5])
            filiere, _ = Filiere.objects.get_or_create(codefiliere=row[0], libellefiliere=row[1],
                                                       dateaccreditation=dateaccreditation, dureeaccreditation=row[3],
                                                       codedept=departement, codeenseignant=enseignant)
            filiere.save()

    with open('Import/etudiant.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            etudiant, _ = Etudiant.objects.get_or_create(numinscription=row[0], nometudiant=row[1], prenometudiant=row[2])
            etudiant.save()

    with open('Import/semestre.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            semestre, _ = Semestre.objects.get_or_create(idsemestre=row[0], libellesemestre=row[1],niveau=row[2])
            semestre.save()

    with open('Import/module.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            filiere , _ = Filiere.objects.get_or_create(codefiliere=row[0])
            semestre, _ = Semestre.objects.get_or_create(idsemestre=row[4])
            enseignant , _ = Enseignant.objects.get_or_create(codeenseignant=row[5])
            module, _ = Module.objects.get_or_create(codefiliere=filiere, codemodule=row[1],libellemodule=row[2],
                                                     naturemodule=row[3],idsemestre=semestre,codeenseignant=enseignant)
            module.save()


    with open('Import/elementmodule.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            filiere, _ = Filiere.objects.get_or_create(codefiliere=row[0])
            module, _ = Module.objects.get_or_create(codemodule=row[1],codefiliere=filiere)

            elementmodule, _ = ElementModule.objects.get_or_create(codefiliere=filiere,codemodule=module,
                                                                   codeelmodule=row[2],libelleelmodule=row[3],
                                                                   coefficient=row[4],vh_cm=(check_number(row[5])),
                                                                   vh_td=check_number(row[6]),vh_tp=check_number(row[7]),
                                                                   vh_ec=check_number(row[8]))
            elementmodule.save()

    with open('Import/naturecours.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            naturecours, _ = Naturecours.objects.get_or_create(typecours=row[0],libellecours=row[1],nbetudiantmax=check_number(row[2]))
            naturecours.save()

    with open('Import/classe.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:

            classe, _ = Classe.objects.get_or_create(codeclasse=row[0],natureclasse=check_number(row[1]))
            classe.save()

    with open('Import/classe_etudiant.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            classe, _ = Classe.objects.get_or_create(codeclasse=row[0])
            etudiant, _ = Etudiant.objects.get_or_create(numinscription=row[1])
            classe_etudiant, _ = ClassEtudiant.objects.get_or_create(codeclass=classe,numinscription=etudiant)
            classe_etudiant.save()