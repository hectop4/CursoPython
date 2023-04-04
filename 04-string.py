name="Hector"
last_name="Puentes"
print(name)
print(last_name)

full_name=name+" "+last_name
print(full_name)


quote="I'm Hector"

quote='She said: "Hello"'

#format

template="Hola, mi nombre es "+ full_name + " es un gusto conocerte"
template2="Mi apellido es {} y mi nombre es {}".format(last_name, name)

template3=f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template3)