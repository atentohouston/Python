groceries = ['Walnuts', 'Grapes', 'Bird seeds']

# Value Indexes

groceries = ['Walnuts', 'Grapes', 'Bird seeds']
# index:         0          1          2

# Alternative Syntax

groceries = [
    'Walnuts',    # index 0
    'Grapes',     # index 1
    'Bird seeds'  # index 2
]

# Indexación de cadenas
# Las cadenas también se pueden indexar. Esto es especialmente útil cuando queremos filtrar ciertas partes de una salida. 
# Podemos pensar en cada palabra como una lista de letras con índices.
# Sin embargo, también existe el índice negativo, que nos permite comenzar a contar las letras de la cadena desde el final.

# example

var = "ABCDEF"
print(var[0], var[1], var[2], var[3], var[4], var[5])
# A B C D E F
print(var[-1], var[-2], var[-3], var[-4], var[-5], var[-6])
# F E D C B A

