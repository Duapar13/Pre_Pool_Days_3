p = "123456789"
print(p[:: -2][:5][:: -1][3:])

# Étape 1: Utilisation de slicing avec un pas négatif de -2
# Cela signifie que nous sélectionnons chaque deuxième caractère, en commençant par le dernier.
# Donc, p[:: -2] renvoie "97531".

# Étape 2: Ensuite, nous utilisons [:5] pour prendre les 5 premiers caractères de la chaîne obtenue précédemment.
# Donc, "97531"[:5] renvoie "97531".

# Étape 3: Ensuite, nous utilisons [:: -1] pour inverser la chaîne obtenue précédemment.
# Donc, "97531"[:: -1] renvoie "13579".

# Étape 4: Enfin, nous utilisons [3:] pour prendre les caractères à partir de l'indice 3 (inclus) jusqu'à la fin.
# Donc, "13579"[3:] renvoie "79".

# Affichage du résultat final