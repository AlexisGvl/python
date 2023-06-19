# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

longueur_max = 0
index_max = 0
valeur_max = ""

for index, valeur in enumerate(my_list):
    longueur = len(valeur)
    if longueur > longueur_max:
        longueur_max = longueur
        index_max = index
        valeur_max = valeur

print(index_max)
print(valeur_max)
print(longueur_max)