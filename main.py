
frutas = []


N = int(input("Ingrese la cantidad de frutas para el salpicón: "))


for i in range(1, N + 1):
    print(f"\nFruta {i}:")
    fruta = {}  
    fruta["id"] = i
    fruta["nombre"] = input("Nombre de la fruta: ")
    fruta["precio_unitario"] = float(input("Precio unitario de la fruta: "))
    fruta["cantidad"] = int(input("Cantidad de la fruta: "))
    frutas.append(fruta)


costo_total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
print("\nEl costo total del salpicón es:", costo_total)


frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"] * x["cantidad"], reverse=True)
print("\nFrutas ordenadas de mayor a menor costo:")
for fruta in frutas_ordenadas:
    print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")


fruta_mas_barata = min(frutas, key=lambda x: x["precio_unitario"])
print("\nLa fruta más barata es:", fruta_mas_barata["nombre"])