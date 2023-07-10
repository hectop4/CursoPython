x=3.3
print(x)
y=1.1+2.2
print(y)
print(x==y)


#Forma de string

y_str = format(y,"2g")
print(y_str==str(x))


#Forma matematica
print('*'*20)

tolerance=0.00001
print(abs(x-y)<tolerance)