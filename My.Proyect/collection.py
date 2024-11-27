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