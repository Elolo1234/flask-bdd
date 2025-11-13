from extensions import db

class Coral(db.Model):
    __tablename__ = "corais"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    localizacao = db.Column(db.String(120), nullable=False)
    especie = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao,
            "especie": self.especie
        }
