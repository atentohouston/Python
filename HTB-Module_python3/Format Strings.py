# cadenas formateadas. Una cadena de formato es una cadena que nos permite llenarla con valores en tiempo de ejecución.
# En Python 3.6 se introdujo una nueva forma de formato: la f-string (como en el ejemplo anterior).
# Mientras que una cadena regular podría verse como 'Hello world'
# una f-string añade una f al principio: f'Hello world'
# La ventaja de la f-string, sin embargo, es que podemos reemplazar partes de la cadena con otros valores y variables encerrándolos entre llaves {}, de esta manera.

equation = f'The meaning of life might be {6 * 7}.'  # -> The meaning of life might be 42.

me = 'Birb'
greeting = f'Hello {me}!'  # -> Hello Birb!

