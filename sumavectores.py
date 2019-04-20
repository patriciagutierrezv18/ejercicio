importar al azar
vector_uno = []
vector_dos = []
vector_suma = []
rango = int ( entrada ( " Ingrese el rango del vector " ))
para i en  rango (rango):
    vector_uno.append (random.randint ( 0 , 20 ))
    vector_dos.append (random.randint ( 0 , 20 ))
para i en  rango ( len (vector_uno)):
    vector_suma.append (vector_uno [i] + vector_dos [i])
Imprimir  " Valores uno: " , vector_uno
Imprimir  " Valores dos: " , vector_dos
imprimir  " resultado: " , vector_suma
