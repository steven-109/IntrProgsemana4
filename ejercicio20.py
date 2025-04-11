total_pagar = float(input("Ingrese el total a pagar por el servicio : "))
propina = 0.15

cal_propina = total_pagar * propina
total_propina = total_pagar + cal_propina


print(f"El total a pagar por su servicio es de : {total_pagar}")
print(f"La propina a pagar por el servicio es de : {cal_propina:.2f}")
print(f"El total a pagar por la propina es de : {total_propina}")