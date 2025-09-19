# 016 Crea un diccionario que represente 
# el catálogo de productos de una tienda, 
# donde las claves son los nombres de los productos 
# y los valores son sus precios.

claveProductos = {
    "Manzana": 1300,
    "Plátano": 1450,
    "Naranja": 900,
    "Leche": 950,
    "Pan": 2500,
    "Huevos": 2500,
    "Arroz": 1500,
    "Pollo": 3000,
    "Carne": 6500,
    "Pescado": 4000
}

def definirProductos(nombre, precio):
    if precio > 0:
        return {nombre.strip().lower(): precio}
    else:
        print("El precio debe ser mayor a 0.")
        return None
    