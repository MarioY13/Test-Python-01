class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        # Validamos que el precio sea mayor que 0 y la cantidad no sea negativa.
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        
        # Atributos privados de la clase Producto
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters: Métodos para acceder a los atributos privados
    def get_nombre(self):
        # Devuelve el nombre del producto
        return self.__nombre

    def get_categoria(self):
        # Devuelve la categoría del producto
        return self.__categoria

    def get_precio(self):
        # Devuelve el precio del producto
        return self.__precio

    def get_cantidad(self):
        # Devuelve la cantidad disponible del producto
        return self.__cantidad

    # Setters: Métodos para modificar los atributos privados con validaciones
    def set_precio(self, nuevo_precio):
        # Actualiza el precio si es mayor que 0, de lo contrario lanza un error
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, nueva_cantidad):
        # Actualiza la cantidad si no es negativa, de lo contrario lanza un error
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self):
        # Representación en texto de un producto, útil para mostrar información
        return f"{self.__nombre} - Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


class Inventario:
    def __init__(self):
        # Lista privada que almacena los productos del inventario
        self.__productos = []

    def agregar_producto(self, producto):
        # Agrega un producto al inventario si su nombre no está repetido
        if not any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            self.__productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al inventario.")
        else:
            print(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        # Busca el producto por nombre y actualiza su precio y/o cantidad
        producto = self.buscar_producto(nombre)
        if producto:
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)  # Cambia el precio si se especifica
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)  # Cambia la cantidad si se especifica
            print(f"Producto '{nombre}' actualizado.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        # Elimina un producto del inventario si lo encuentra
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        # Con esto vemos todos los productos en el inventario
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            for producto in self.__productos:
                print(producto)  # Usa la representación en texto del producto

    def buscar_producto(self, nombre):
        # Busca un producto por nombre en la lista
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto  # Devuelve el producto si se encuentra
        print(f"Producto '{nombre}' no encontrado.")
        return None
  