presion = float(input("Ingrese el valor de la presion : "))
volumen = float(input("Ingrese el valor del volumen : "))
temperatura = float(input("Ingrese el valor de la temperatura : "))

masa = (presion * volumen) / (0.37(temperatura + 460))

print(f"El valor de la masa es de : {masa}")