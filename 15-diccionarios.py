#[] list
#() tuple
#{} dictionary

my_dict={}

print(my_dict)
print(type(my_dict))
my_dict={

    'name':'Juan ',
    'last_name':'Perez',
    'age': 28,
    
    }
print(my_dict)

print(len(my_dict))

print(my_dict['name'])
print(my_dict['last_name'])#Solo funciona si la llave existe
print(my_dict.get('age'))#Funciona si la llave no existe, y retorna un NONE
print('avion'in my_dict)#Verifica si existe la llave en el diccionario
print('name'in my_dict)