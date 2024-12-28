import mysql.connector

conn = mysql.connector.connect(
    host="db5016915206.hosting-data.io",
    user="dbu5492153",
    password="M4f3mm33stf4nt4st!qu3",
    database="dbs13643632",
    port=3306,
    connection_timeout=10  # Timeout de 10 secondes
)

cursor = conn.cursor()

# Création d'une table
cursor.execute("""
CREATE TABLE IF NOT EXISTS produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prix DECIMAL(10, 2)
)
""")

# Insertion de données
cursor.execute("INSERT INTO produits (nom, prix) VALUES (%s, %s)", ("Produit1", 19.99))

# Lecture des données
cursor.execute("SELECT * FROM produits")
resultats = cursor.fetchall()
for ligne in resultats:
    print(ligne)

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()