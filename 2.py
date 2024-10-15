string = input('Digite uma sequência de caracteres: ')

amount = string.lower().count('a')

if amount == 0:
    print("Não existem letras 'a' na string")
else:
    print(f"Existem {amount} letras 'a' na string")