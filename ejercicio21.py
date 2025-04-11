producto1 = float(input("Ingrese el valor del producto 1 :"))
producto2 = float(input("Ingrese el valor del producto 2 :"))
producto3 = float(input("Ingrese el valor del producto 3 :"))


subtotal = producto1 + producto2 + producto3
sub_iba = subtotal * 0.15
total = subtotal + sub_iba

print(f"El subtotal es de :{subtotal} ")
print(f"El iva masa el producto es de : {sub_iba}")
print(f"El total a pagar es de : {total}")