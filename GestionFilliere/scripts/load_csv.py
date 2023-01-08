
from datetime import datetime

from ..models import *
import csv


def run():

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



