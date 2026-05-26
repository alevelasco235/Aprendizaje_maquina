#Escribe un programa que solicite al usuario su calificación final y determine si ha aprobado o reprobado. Considera que la calificación mínima para aprobar es 7.  
calificacion = int(input("Ingresa tu calificacion final\n"))
#El programa evalúa si la calificación es mayor o igual a 7, en ese caso se imprime "Aprobado", de lo contrario se imprime "Reprobado".
if calificacion >= 7:
    print("Aprobado")
#En caso de que la calificación sea menor a 7, se imprime "Reprobado".
else:   
    print("Reprobado")