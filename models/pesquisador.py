from extensions import db

class Pesquisador(db.Model):
    __tablename__ = "pesquisadores"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    area = db.Column(db.String(200), nullable=True)

    def __init__(self, nome, area=None):
        self.nome = nome
        self.area = area

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "area": self.area}

    def __repr__(self):
        return f"<Pesquisador nome={self.nome} area={self.area}>"
