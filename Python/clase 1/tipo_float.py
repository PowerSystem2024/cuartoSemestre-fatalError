#profundidad en el tipo float
a = 3.0
print(f"a:{a:.2f}")

#consutrctor de tipo float -> puede recibir int y str
a = float(10) #le pasamos un tipo entero
a = float('10')
print(f"a:{a:2f}")

#Notacion exponencial (valores positivos o negativos)
a = 3e5
print(f'a:{a:.2f}')

a = 3e-5
print(f'a: {a:.5f}')

#cualquier calculo que incluyte un float , todo cambia a float
a = 4.0+5
print(a)
print(type(a))


