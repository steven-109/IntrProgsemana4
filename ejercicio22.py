tareas = float(input("Ingrese la calificacion de la tarea del estudiante : "))
examen_parcial = float(input("Ingrese la calificacion del examen parcial de el estudiante"))
examen_final= float(input("Ingrese la calificacion del examen final de el estudiante : "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

print(f"La calificacion final de el estudiante es de : {calificacion_final}")