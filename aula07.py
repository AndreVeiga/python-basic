numero = 0

while numero < 10:
    print(numero)

    if numero == 11:
        print("Break!")
        break
    
    numero += 1
else:
    print("Igual que 10")