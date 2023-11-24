#!/usr/bin/python3
import MySQLdb
import sys

# Vérifiez si le nombre d'arguments est correct
if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

# Récupérez les informations de connexion depuis les arguments
MY_USER = sys.argv[1]
MY_PASSWORD = sys.argv[2]
MY_DB = sys.argv[3]
MY_HOST = 'localhost'

# Établir la connexion à la base de données
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd='', db=MY_DB)

# Créer un objet curseur pour exécuter des requêtes
cur = db.cursor()

# Exécuter la requête SQL pour sélectionner tous les états
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Récupérer les résultats et les afficher
results = cur.fetchall()
for row in results:
    if row[1].startswith('N'):
        print(row)

# Fermer le curseur et la connexion à la base de données
cur.close()
db.close()
