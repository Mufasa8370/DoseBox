import requests

def fetch_data():
    # URL du fichier PHP
    url = "https://dev-henin.com/serenity/get_table.php"  # Remplacez par l'URL de votre fichier PHP

    try:
        # Envoyer la requête GET
        response = requests.get(url, timeout=5)

        # Vérifier le statut de la réponse
        if response.status_code == 200:  # 200 OK
            # Récupérer la réponse en JSON
            data = response.json()

            # Afficher la réponse
            print("Réponse du serveur :")
            print(data)
        else:
            print(f"Erreur HTTP : {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Gérer les exceptions liées à la requête
        print(f"Erreur : {e}")

if __name__ == "__main__":
    fetch_data()