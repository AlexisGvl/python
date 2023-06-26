# exo 9.10
# En utilisant une boucle `for` et la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.10


for key, value in my_dict.items():
    print(f"{key = }")
    print(f"{value = }")
