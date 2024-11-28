from str2Doc import Str2Doc
from document import Document

class Collection:
    def __init__(self, name):
        self.name = name
        self.documents = {}
    
    def add_document(self, document):
        self.documents[document.id] = document
    
    def delete_document(self, id_document):
        if id_document in self.documents:
            del self.documents[id_document]
    
    def search_document(self, id_document):
        return self.documents.get(id_document, None)
    
    def __str__(self):
        return f"Collecion {self.name} con {len(self.documents)} documentos"
    ###########
    def import_from_csv(self, rutacsv): 
        with open(rutacsv, 'r') as file: 
            contenido = file.readline().replace('\n', '') #Reemplazar el \n(saltodelinea) por caracter vacío  
            str2 = str2Doc(contenido)  
            linea = file.readline() 
            incremental = 0 
            while linea != "": 
                nuevo_doc = Document(incremental, str2.convert(linea.strip('\n'))) 
                self.add_document(nuevo_doc) 
                incremental = incremental + 1 
                linea = file.readline()