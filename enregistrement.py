# enregistrement.py
import csv
from datetime import datetime

FICHIER_CSV = "candidatures.csv"

# Crée l'entête du fichier s'il n'existe pas encore
def initialiser_csv():
    try:
        with open(FICHIER_CSV, mode='x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Nom', 'Email', 'Compétences', 'Score', 'Date'])
    except FileExistsError:
        pass  # Le fichier existe déjà

# Enregistre une ligne de candidature dans le fichier CSV
def enregistrer_candidature(nom, email, competences, score):
    with open(FICHIER_CSV, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nom, email, competences, score, datetime.now().isoformat()])

# Appel au démarrage pour s'assurer que le fichier existe
initialiser_csv()
