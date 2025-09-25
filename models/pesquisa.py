class Pesquisa:
    def __init__(self,id, titulo, objetivo, ano, local, coral_relacionado):
        self.id = id 
        self.titulo = titulo
        self.objetivo = objetivo
        self.ano = ano
        self.local = local
        self.coral_relacionado = coral_relacionado

    def to_dict(self):
        return {
            "id": self.id, 
            "titulo": self.titulo,
            "objetivo": self.objetivo,
            "ano": self.ano,
            "local": self.local,
            "coral_relacionado": self.coral_relacionado
        }
