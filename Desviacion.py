
n = int(raw_input('La cantidad de datos es: '))
datos = []
i = 0
while i < n:
  d = float(raw_input('El siguiente dato es: ')) #Agrego todos los elementos a la lista de datos
  datos.append(d)
  i += 1
promedio = sum(datos)/n 
cuadrados = [] #lista de la suma de los cuadrados de las diferencias entre los datos y el promedio
for dato in datos:
  r = (dato - promedio)**2
  cuadrados.append(r)
desviacion = (sum(cuadrados)/(n - 1))**0.5 #fórmula de desviación estándar
print 'El promedio es', promedio
print 'La desviación estándar es', desviacion
