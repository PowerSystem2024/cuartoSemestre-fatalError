from mi_clase import MiClase

#help(MiClase) #asi podemos ver toda la info 

#print(MiClase.__doc__) #apunta solo a la clase

#print(MiClase.__init__.__doc__) #apunta al init

#print(MiClase.mi_metodo.__doc__) #apunta al metodo
print(MiClase.mi_metodo) # apunta al lugar que ocupa dentro de la memoria
print(type(MiClase.mi_metodo)) #nos dice a que clase pertenece, en este caso, es una funcion
