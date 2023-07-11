person={
    'name':'Juan ',
    'last_name':'Perez',
    'langs':['Python','Java','JavaScript'],
    'age': 28,
}
print(person)

person['age']=29
print(person)
person['langs'].append('C#')
print(person)


del person['age']
print(person)

person.pop('last_name')
print(person)



print(person.items())# Retorna los items del diccionario
print(person.keys())# Retorna las llaves del diccionario
print(person.values())# Retorna los valores del diccionario
