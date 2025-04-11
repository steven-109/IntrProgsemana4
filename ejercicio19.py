producto = int(input("Ingrese el nombre del producto : "))
precio = float(input("Ingrese el precio del producto"))   
descuento = 0.10

desc_produc = precio * descuento
total_produc = precio - desc_produc

print(f"El nombre del producto es : {producto}")
print(f"El precio del producto es : {precio}")
print(f"El precio final del producto es : {total_produc}")