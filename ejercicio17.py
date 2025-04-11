alumnos = int(input("Ingrese la cantidad total de alumnos : "))
hombres = int(input("Ingrese la cantidad de hombres que hay en el salon : "))
mujeres = int(input("Ingrese la cantidad de mujeres que hay en el salon :"))


porc_hombres = (hombres/alumnos) * 100
porc_muj = (mujeres/alumnos) * 100

print(f"La cantidad total de alumnos que hay en el salon es de : {alumnos}")
print(f"La cantidad de hombres en el salon es de :{hombres}")
print(f"La cantidad de mujeres en el salon es de : {mujeres}")
print(f"El porcentaje total de hombres que hay en el salon es de : {porc_hombres}%")
print(f"El porcentaje total de mujeres que hay en el salon es de :{porc_muj}%")