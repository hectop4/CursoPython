#continue Continua con la siguiente iteracion saltando las demas lineas de codigo debajo de el
#break Termina el ciclo

#for element in range(5,20):
 #   print(element)


my_list=[54,23,6,7,3,1,123,75,68,12]

for element in my_list:
    print(element)


my_tuple=(54,23,6,7,3,1,123,75,68,12)

for element in my_tuple:
    print(element)
my_dict={'name':'Camisa','Price':15000,'stock': 28,}
for element in my_dict:
    print(my_dict[element])


for key,value in my_dict.items():
    print(key,value)


people=[{'name':'Juan','age':28,'address':'Bogota'},
        {'name':'Maria','age':25,'address':'Medellin'},
        {'name':'Pedro','age':30,'address':'Cali'}]

for person in people:
    print(person)
    print(person['name'])