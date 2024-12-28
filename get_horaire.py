import requests
import json
import time
from datetime import datetime
import os
from crontab import CronTab

# Fonction pour récupérer les données depuis le serveur
def fetch_data():
    url = "https://dev-henin.com/serenity/get_table.php"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            # Sauvegarder les horaires dans un fichier JSON
            with open('config.json', 'w') as f:
                json.dump(data, f, indent=4)

            print("Heures sauvegardées dans config.json")
        else:
            print(f"Erreur HTTP : {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur : {e}")

# Charger les horaires depuis le fichier config.json
def load_schedule():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            return json.load(f)
    else:
        print("Le fichier de configuration n'existe pas.")
        return []

# Mettre à jour la crontab avec les horaires dynamiques
def update_crontab():
    schedule = load_schedule()  # Charger les horaires depuis le fichier config.json

    # Créer un objet CronTab pour l'utilisateur courant
    cron = CronTab(user=True)

    # Supprimer les anciennes tâches cron (optionnel, si vous voulez tout réinitialiser à chaque fois)
    cron.remove_all()

    # Parcourir chaque horaire et ajouter une tâche cron
    for item in schedule:
        hour, minute, _ = item['time'].split(':')  # Extraire l'heure et les minutes
        cron_command = f"/usr/bin/python3 /chemin/vers/votre_script.py"  # Remplacer par le chemin de votre script à exécuter

        # Ajouter l'entrée cron à l'heure et minute spécifiées
        job = cron.new(command=cron_command)
        job.setall(f"{minute} {hour} * * *")  # Heure et minute

    # Sauvegarder les modifications dans la crontab
    cron.write()
    print("Tâches cron mises à jour avec succès.")

# Fonction principale
if __name__ == "__main__":
    fetch_data()  # Récupérer et stocker les horaires dans config.json
    update_crontab()  # Mettre à jour la crontab avec les horaires extraits du fichier config.json
