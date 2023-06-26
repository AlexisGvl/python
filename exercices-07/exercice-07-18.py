# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

import random

# réponse 7.18

import random

r = random.randint(1, 100)
while r != 100:
    print(r)
    r = random.randint(1, 100)
print(100)
