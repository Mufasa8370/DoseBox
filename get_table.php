<?php
// Paramètres de connexion à la base de données
$host = "db5016915206.hosting-data.io";  // Remplacez par votre hôte
$dbname = "dbs13643632";  // Remplacez par le nom de votre base de données
$username = "dbu5492153";  // Remplacez par votre nom d'utilisateur
$password = "Maf3mm33stf4nt4st!qu3";  // Remplacez par votre mot de passe

// Créer une connexion à la base de données MySQL
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Définir le mode d'erreur de PDO
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Requête SQL pour récupérer les données de la table 'produits'
    $sql = "SELECT * FROM horaire";
    
    // Exécuter la requête et récupérer les résultats
    $stmt = $pdo->query($sql);
    
    // Récupérer toutes les lignes sous forme de tableau associatif
    $produits = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Renvoyer les résultats en JSON
    echo json_encode($produits);

} catch (PDOException $e) {
    // Gérer les erreurs de connexion
    echo "Erreur de connexion : " . $e->getMessage();
}
?>
