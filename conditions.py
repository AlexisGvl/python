import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(f'{number1 = }')
print(f'{number2 = }')

# block if1
if number1 < number2 :
    print("La variable number1 est plus petite que number2")

# block if2
if number1 < number2 :
    print("La variable number1 est plus petite que number2")
else: #number1 >= number2
    print("La variable number1 est plus grande ou égale à number2")

# block if3
if number1 < number2 :
    print("La variable number1 est plus petite que number2")
elif number1 > number2 :
    print("La variable number1 est plus grande que number2")
else :
    print("Les 2 variables number1 et number2 sont égales")

# elif == else if

#block if4
# réécriture du block if3 avec des if imbriqués

if number1 < number2 :
    print("La variable number1 est plus petite que number2")
else :
    if number1 > number2 :
        print("La variable number1 est plus grande que number2")
    else :
        print("Les 2 variables number1 et number2 sont égales")

# opérateurs booléens

# négation
print(not True)
print(not False)

# Table de vérité de l'opérateur de négation
# A     not A
# True  False
# False  True

# OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Table de vérité de l'opérateur OU logique
# A     B       A or B
# True  True    True
# True  False   True
# False True    True
#False  False   False       

# pour retrouver la table, remplacez :
# "A" par "j'ai du cash"
# "B" par "j'ai ma cb"
# "A or B" par "puis-je faire mes courses ?"

# ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Table de vérité de l'opérateur OU logique
# A     B       A and B
# True  True    True
# True  False   False
# False True    False
# False  False  False     


# table de vérité de l'opérateur NAND (not and)
# A     B       A and B not (A and B)
# True  True    True    False
# True  False   False   True
# False True    False   True
# False  False  False   True  

# utilisation de l'opérateur and pour voir si une variable est dans un interval de valeurs

# OU exclusif

print(True^True)
print(True^False)
print(False^True)
print(False^False)

# table de vérité de l'opérateur XOR
#   A       B       A ou B
#   True    True    False
#   True    False   True
#   False   True    True
#   False   False   False

# exo course (opérateur OU logique)
# affichez 
# - "je peux aller faire les courses" si j'ai au moins un moyen de paiement
# - "je ne peux pas aller faire les courses" si je n'ai aucun moyen de paiement
has_cash = bool (random.randint(0,1))
has_cb = bool (random.randint(0,1))

print (f'{has_cash = }')
print (f'{has_cb =}')

if has_cash or has_cb :
    print('Je peux aller faire mes courses.' )
else :
    print('Je ne peux pas aller faire mes courses.')

# exo courses (opérateur ET logique)
# remplissez le même cahier des charges mais avec l'opérateur ET logique
    
    has_cash = bool (random.randint(0,1))
has_cb = bool (random.randint(0,1))

print (f'{has_cash = }')
print (f'{has_cb =}')

# version naïve

if has_cash == False and has_cb == False :
    print('Je ne peux pas aller faire mes courses')
else :
    print('Je peux aller faire mes courses')

# version optimisée

if not has_cb and not has_cash :
    print('Je ne peux pas aller faire mes courses')
else :
    print('Je peux aller faire mes courses')

# combinaison d'opérateurs AND et OR
user_level = 1
user_xp = 0
user_social = 150

# version buggée
if user_level >= 3 and user_xp >= 100 or user_social >= 100 :
    print('Le joueur peut acheter du matériel')
else :
    print('Le joueur ne peut pas acheter de matériel')

#version corrigée
if user_level >= 3 and (user_xp >=100 or user_social >= 100) :
    print('Le joueur peut acheter du matériel')
else :
    print('Le joueur ne peut pas acheter de matériel')

# exo carte de réduction
# déterminer la carte de réduction auquelle le voyageur a droit :
# - entre 0 et 11 ans inclus, le voyageur a droit à la gratuité
# - entre 12 et 25 ans inclus, le voyageur a droit à une réduction de 50%
# - entre 26 et 64 ans inclus, le voyageur a droit à une réduction de 10%
# - au-delà de 65 ans inclus, le voyageur a droit à une réduction de 50%

age = random.randint(0, 99)
print(age)
 # méthode souhaitée, car entièreté du cahier des charges apparente

 if age >= 0 and age <= 11 :
    print('gratuité')
elif age >= 12 and <= 25 :
    print ('50%')
elif age >= 26 and age <=64 :
    print('10%')
elif age >= 65 and age <= 99 :
    print('50%')

# méthode, optimisée mais compliquée à corriger pour une autre personne

if age <= 11 :
    print('le voyageur a droit à la gratuité')
elif 26<= age <= 64 :
    print('le voyageur a droit à une réduction de 10%')
else :
    print('le voyageur a droit à une réduction de 50%')















    
