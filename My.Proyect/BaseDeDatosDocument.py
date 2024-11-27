from document import Document
from collection import Collection

class BaseDeDatosDocumental:
    def __init__(self):
        self.colecciones = {}
    
    def create_collection(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
    
    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def get_collection(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones" 
    