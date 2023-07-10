text='Ella sabe programar en Python'


# 1. Verficar si la palabra 'Python' está en la variable text
print('Python' in text)

# 2. Tamaño de la variable text

print(len(text))

#3. Pasar texto a mayúsculas

print(text, text.upper())

#4. Pasar texto a minúsculas
print(text, text.lower())

#5. Contar numero de apariciones

print(text.count('a'))

#6.Cambiar mayúsculas por minúsculas y viceversa

print(text.swapcase())

#7. Corroborar si el texto empieza con 'Ella'

print(text.startswith('Ella'))

#8. Corroborar si el texto termina con 'Rust'
print(text.endswith('Rust'))

#9. Reemplazar cadenas de texto

print(text.replace('Python', 'Rust'))


#10. Capitalizar texto

text_2="hola mundo de programadores"

print(text_2.capitalize())

#11. Capitalizar cada palabra

print(text_2.title())

#12. Corroborar si es un digito
print(text_2.isdigit())
print('123'.isdigit())