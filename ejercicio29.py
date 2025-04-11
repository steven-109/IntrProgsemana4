presupuesto = float(input("Ingrese el presupuesto inicial : "))

urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print(f"El presupuesto para el area de urgencias es de : {urgencias:.2f}")
print(f"El presupuesto para el area de pediatria es de : {pediatria:.2f}")
print(f"El presupuesto para el area de traumatologia es de : {traumatologia:.2f}")