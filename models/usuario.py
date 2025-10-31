from extensions import db

# ...existing code...
class Pesquisador(db.Model):
    __tablename__ = "pesquisadores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    area = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "area": self.area}
# ...existing code...