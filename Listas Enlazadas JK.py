class Delito:
    def __init__(self, tipo, fecha, lugar):
        self.tipo = tipo
        self.fecha = fecha
        self.lugar = lugar
        self.siguiente = None

class ListaDelitos:
    def __init__(self):
        self.primero = None

    def agregar_delito(self, tipo, fecha, lugar):
        """Agrega un nuevo delito al final de la lista enlazada."""
        nuevo_delito = Delito(tipo, fecha, lugar)
        if self.primero is None:
            self.primero = nuevo_delito
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_delito

    def eliminar_delito(self, tipo):
        """Elimina el primer delito que coincida con el tipo dado."""
        if not self.primero:  # La lista está vacía
            print("La lista de delitos está vacía.")
            return False

        actual = self.primero
        anterior = None
        while actual:
            if actual.tipo == tipo:
                if anterior is None:  # Si el delito a eliminar es el primero
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False  # No se encontró el delito

    def mostrar_delitos(self):
        """Muestra todos los delitos en la lista."""
        if not self.primero:
            print("No hay delitos registrados.")
            return

        actual = self.primero
        print("Lista de delitos registrados:")
        while actual:
            print(f"Tipo: {actual.tipo}, Fecha: {actual.fecha}, Lugar: {actual.lugar}")
            actual = actual.siguiente

    def eliminar_multiples_delitos(self):
        """Permite eliminar múltiples delitos de manera interactiva."""
        while True:
            if not self.primero:
                print("\nNo hay más delitos en la lista para eliminar.")
                break

            # Mostrar la lista actualizada antes de cada eliminación
            print("\nLista actualizada de delitos:")
            self.mostrar_delitos()

            # Pedir al usuario el tipo de delito a eliminar
            tipo_a_eliminar = input("\nIngrese el tipo de delito a eliminar (o escriba 'salir' para terminar): ")
            if tipo_a_eliminar.lower() == 'salir':
                print("\nFinalizando el proceso de eliminación.")
                break

            # Intentar eliminar el delito
            if self.eliminar_delito(tipo_a_eliminar):
                print(f"El delito de tipo '{tipo_a_eliminar}' ha sido eliminado correctamente.")
            else:
                print(f"No se encontró ningún delito de tipo '{tipo_a_eliminar}'.")
        
        print("\nProceso de eliminación de múltiples delitos finalizado.")


# Crear una lista de delitos
lista_delitos = ListaDelitos()

# Agregar algunos delitos
lista_delitos.agregar_delito("Robo de celular", "2023-11-25", "Calle Principal")
lista_delitos.agregar_delito("Asalto a mano armada", "2023-12-01", "Parque Central")
lista_delitos.agregar_delito("Robo de vehículos", "2024-01-15", "Supermercado")
lista_delitos.agregar_delito("Robo de celulares", "2024-01-20", "Estación de tren")

# Mostrar todos los delitos registrados
print("\nDelitos iniciales:")
lista_delitos.mostrar_delitos()

# Iniciar el proceso interactivo de eliminación de múltiples delitos
print("\n*** Eliminar múltiples delitos ***")
lista_delitos.eliminar_multiples_delitos()

# Mostrar la lista actualizada después de eliminar
print("\nLista final de delitos:")
lista_delitos.mostrar_delitos()
