numbers=[1,2,3,4]
print(numbers)
tasks=['lavar platos', 'Jugar videojuegos', 'Dar amor']
print(tasks)
types=[1,True,'Hola']
print(types)

print(numbers[0])
print(tasks[0])

#mutaciones
#Los string no son mutables
#text='Hola'
#text[0]='w'
tasks[0]="Divertirme"
print(tasks)

print(True in types)
print('Hola'in types)