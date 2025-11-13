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
from extensions import db

class Pesquisa(db.Model):
    __tablename__ = "pesquisas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    objetivo = db.Column(db.String(500), nullable=True)
    ano = db.Column(db.Integer, nullable=True)
    local = db.Column(db.String(200), nullable=True)
    coral_relacionado = db.Column(db.String(200), nullable=True)

    def __init__(self, titulo, objetivo, ano, local, coral_relacionado):
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
