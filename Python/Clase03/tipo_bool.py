#Bool contiene los valroes de True y False
#Los tipo numericos, es false para el 0(cero), true para los demas valores

valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}') #cualquier numero fuera del 0 es True

#Tipo string -> False '', True demas valores 
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tipo colecciones -> False para colecciones vacias 
#Tipo colecciones -> Ture para todas las demas

#Lista 
valor = []
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')


valor = [2,3,4]
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = {'Nombre':'Juan'}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Sentencias de control con bool 
if bool('hola'): #si tiene valor
    print('Regresa verdadero')
else:
    print('Regresa falso')
    
#ciclos
variable = 3
while variable: 
    print(f'valor: {valor}, Resultado: {resultado}')
    break
else:
    print(f'valor: {valor}, Resultado: {resultado}')