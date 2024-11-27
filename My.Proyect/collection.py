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
    def import_from_csv(self, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                doc_id = row['id'] 
                contenido = {key: value for key, value in row.items() if key != 'id'} 
                document = Document(doc_id, contenido) 
                self.add_document(document)