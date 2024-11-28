
class Str2Doc (object):
    def __init__ (self, schema, separator=","):
        self.separator = separator
        self.keys = schema.split(separator)
    def convert(self, line):
        values = line.split(self.separator)
        if len(values) == len(self.keys):
            diccionario = {}
            i = 0
            while i < len(self.keys):
                diccionario[self.keys[i]] = values[i]
                i = i + 1
            return diccionario
