#help(str.split)
cursos = 'Java JavaScrip Node Python Diseno'
lista_cursos = cursos.split() #hace una lista
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

'''
cursos_separados_coma = 'Java,Python,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split()
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos)) # es un solo elemento 
'''
'''
cursos_separados_coma = 'Java,Python,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',')# para que reconozca la coma y divida los elementos
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos)) #ahora si divide los elementos
'''

cursos_separados_coma = 'Java,Python,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',' ,2)# para que reconozca la coma y reconozca los elmentos 0,1,2
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos)) #ahora si divide los elementos