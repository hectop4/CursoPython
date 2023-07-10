#CRUD=> Create,Read, Update & Delete

numbers=[1,2,3,4,5,6,7]  #create
print(numbers[3])   #Read

numbers[-1]=2       #Update

#Delete
numbers.append(700) # Agrega 700 a la lista
print(numbers)
numbers.insert(0,'Hola') #inserta hola en la posicion 0 # type: ignore
print(numbers)

numbers.insert(3,"Cambio") # type: ignore
print(numbers)

tasks=["Tocar el piano","Dar carro","No se"]

new_list=numbers+tasks # se unen las listas

print(new_list)

print(new_list.index("Cambio"))
index=new_list.index("Cambio")# obtinene la posicion de Cambio en la lista
new_list[index]="Cambio de task"
print(new_list)

new_list.remove('Hola') #Quita el hola de la lista
print(new_list)

new_list.pop() # Elimina el ultimo elemento de la lista
print(new_list)

new_list.pop(0) #Elimina el elemento de la posicion 0 de la lista
print(new_list)


new_list.reverse()
print(new_list)

numbers_a=[1,6,4,8,8,4,3,78,90,5,1]#Ordena la lista de menor a mayor
numbers_a.sort()
print(numbers_a)

strings=['re','ase','ehg']#Ordena la lista de menor a mayor
strings.sort()
print(strings)