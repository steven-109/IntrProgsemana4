lunes = float(input("Ingrese el tiempo recorrido el dia lunes :"))
martes = float(input("Ingrese el tiempo recorrido el dia martes :"))
miercoles = float(input("Ingrese el tiempo recorrido el dia miercoles : "))

tiempo_total = (lunes + martes + miercoles)/3

print(f"El tiempo total recorrido en los dias lunes, martes y miercoles es de : {tiempo_total:.2f}")