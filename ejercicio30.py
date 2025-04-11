nombre = input("Ingrese su nombre :")
horas_trabajadas = int(input("Ingrese el total de horas trabajadas : "))
precio_cobrante = float(input("Ingrese el precio que cobra por hora : "))

sueldo_bruto = precio_cobrante * horas_trabajadas
desc_ir = sueldo_bruto * 0.05
salario_pagar = sueldo_bruto - desc_ir

print(f"El nombre del trabajador es : {nombre}")
print(f"El sueldo bruto es de : {sueldo_bruto}")
print(f"El descuento sobre la renta es de : {desc_ir}")
print(f"El salario a pagar al trabajador es de : {salario_pagar}")