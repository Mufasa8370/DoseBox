from datetime import datetime

# Afficher l'heure et la date actuelles
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format : année-mois-jour heure:minute:seconde

# Afficher le message avec l'heure actuelle
print(f"cron - Heure actuelle : {current_time}")
