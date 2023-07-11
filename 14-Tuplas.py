numbers=(1,2,3,4,5,6,7)  
strings=('re','ase','ehg')
print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

print(numbers[0])

#CRUD=> Create, Read, Update, Delete in lists
#For tuples only Read.


print(numbers)

#methods

print(strings.index('re'))

print(numbers.count(1))
#Convert tuple to list
my_list=list(strings)

print(my_list)

my_list[1]='new' # type: ignore
print(my_list)
#Convert list to tuple
my_tuple=tuple(my_list)

print(my_tuple)




