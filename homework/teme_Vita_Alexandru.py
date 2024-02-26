                # Tema modul 4
# Exercise 1

for x in range(10, 21):
    y = 3 * x
    result = 3 * x ** 2 - 4 * y + 4
    print(f'========{x}=======')
    print(f'Rezultatul functie este : {result}')

# Exercise 2 + 3

nr_carti = int(input("Cati carti doriti sa adaugati in biblioteca? "))
lista_carti = []

for i in range(1, nr_carti + 1):
    print(f'=====Cartea {i} =====')
    nume_carte = input("Numele cartii :")
    autor_carte = input('Autorul este :')
    anul_publicarii = input("Anul publicari este :")
    info_carti = {'Nume': nume_carte, 'Autor': autor_carte, 'Anul': anul_publicarii}
    lista_carti.append(info_carti)

print('Cartile dumneavoastra sunt : ')
for info in lista_carti:
    print(info)

an_cautat = int(input('Alege anul publicarii :'))
print(f'Anul publicari ales este : {an_cautat}')


for an in lista_carti:
    if int(an['Anul']) > an_cautat:
        print(an)


# Tema loto 6/49

import random

input_utilizator = input('Introduceti 6 numere separate prin virgula [1-49] : ')
numere_alese_str = input_utilizator.split(',')
numere_alese_lista = []


for numere_str in numere_alese_str:
    numar = int(numere_str)
    if 1 <= numar <= 49:
        numere_alese_lista.append(numar)
if len(numere_alese_lista) != 6:
    print('Nu ati introdus 6 numere valide')
    exit()

print(numere_alese_lista)


random_extragere_num = random.sample(range(1, 50), 6)       # where k means : count

numere_ghicite = 0
numere_alese_unice = []


for n in numere_alese_lista:
    if n not in numere_alese_unice:
        numere_alese_unice.append(n)


for n in numere_alese_unice:
    if n in random_extragere_num:
        numere_ghicite += 1


print(f'Numere alese sunt : {numere_alese_lista}')
print(f'Numere extrase sunt : {random_extragere_num}')
print(f'Ati ghicit atatea numere : {numere_ghicite}')


if numere_ghicite == 3:
    print('Castig : 50 de lei')
elif numere_ghicite == 4 or numere_ghicite == 5:
    print('Castig : 500 lei')
elif numere_ghicite == 6:
    print('Felicitari ! Ai castigat 1500 lei')
else:
    print('Mai incearca , nu ai castigat nimic')