class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters con validaciones
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self):
        return f"{self.__nombre} - Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if not any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            self.__productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al inventario.")
        else:
            print(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        producto = self.buscar_producto(nombre)
        if producto:
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            print(f"Producto '{nombre}' actualizado.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        print(f"Producto '{nombre}' no encontrado.")
        return None


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    try:
        # Crear productos
        producto1 = Producto("Laptop", "Electrónica", 1500, 10)
        producto2 = Producto("Mouse", "Accesorios", 20, 50)

        # Agregar productos al inventario
        inventario.agregar_producto(producto1)
        inventario.agregar_producto(producto2)

        # Mostrar inventario
        inventario.mostrar_inventario()

        # Buscar producto
        producto_buscado = inventario.buscar_producto("Laptop")
        if producto_buscado:
            print("Producto encontrado:", producto_buscado)

        # Actualizar producto
        inventario.actualizar_producto("Laptop", nuevo_precio=1400, nueva_cantidad=8)

        # Eliminar producto
        inventario.eliminar_producto("Mouse")

        # Mostrar inventario después de eliminación
        inventario.mostrar_inventario()

    except ValueError as e:
        print("Error:", e)
