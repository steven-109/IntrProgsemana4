prestamo = int(input("Ingrese la cantidad de prestamo del banco : "))
tasa = float(input("Ingrese la tasa anual que cobra el banco : "))

interes = prestamo * tasa * 1
monto_total = prestamo + interes
print(f"El prestamo realizado al banco es de: {prestamo}")
print(f"La tasa anual que cobra el banco es de : {tasa}")
print(f"El interes que debera pagar es de : {monto_total}")