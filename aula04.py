numbers = [0, 2, 4]
numbers2 = [6, 8, 10]

numbers += numbers2

print(numbers) # lista concatenada
print(numbers[0]) # 1° valor

# Formas de imprimir os valores
print(numbers[0:4])
print(numbers[:4])
print(numbers[4:])

numbers.append(8) # Adicionando valores

print(numbers)
del(numbers[2])
print(numbers)
