salario_act = int(input("Ingrese el salario actual de el empleado :"))
incremento = float(input("Ingrese el porcentaje de incremento al salario : "))
desc_servi = float(input("Ingrese el descuento total por servicios"))

salario_total = salario_act + (salario_act * incremento) - (salario_act * desc_servi)

print(f"El salario base del empleado es de : {salario_act}")
print(f"El incremento al salario es de : {incremento} ")
print(f"El descuento por servicio es de : {desc_servi}")
print(f"El salario final es de : {salario_total}")