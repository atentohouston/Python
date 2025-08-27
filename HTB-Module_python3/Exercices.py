# What is the result of running the code in "Code block"?

#list_3 = ['Accidental', '4daa7fe9', 'eM131Me', 'Y!.90']
#secret = []

#for x in list_3:
#    secret.append(x[:2])

#print(''.join(secret))


# Análizis:

# Lista 
list_3 = ['Accidental', '4daa7fe9', 'eM131Me', 'Y!.90']

# Lista vacía secret
secret = []

# Se prepara para guardar resultados parciales.
for x in list_3:  # → recorre cada elemento de list_3 uno por uno.
    secret.append(x[:2]) # → toma los dos primeros caracteres del elemento actual. y añade esos dos caracteres a la lista secret.

# Iteraciones: 

#'Accidental'[:2] → 'Ac' → secret = ['Ac']
#'4daa7fe9'[:2] → '4d' → secret = ['Ac', '4d']
#'eM131Me'[:2] → 'eM' → secret = ['Ac', '4d', 'eM']
#'Y!.90'[:2] → 'Y!' → secret = ['Ac', '4d', 'eM', 'Y!']

print(''.join(secret)) # → une todos los elementos de la lista sin espacios.