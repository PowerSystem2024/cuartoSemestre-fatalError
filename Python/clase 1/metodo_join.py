#help(str.join)

tupla_str = ('Hola ', 'Estudiantes ', 'Tecnicatura ','Universitaria')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}') #devuelve una sola cadena

lista_cursos = ['Java','Python','Angular','Spring']

mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre':'Juan','apellido': 'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys()) #agrega un guion al finalizar cada llave
valores = '-'.join(diccionario.values()) #agrega un guion al finalizar cada valor
print(f'Llaves: {llaves}, Type: {type(llaves)}')
print(f'Valores: {valores}, Type: {type(valores)}')