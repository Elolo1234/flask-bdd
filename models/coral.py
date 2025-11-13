from extensions import db

class Coral(db.Model):
    __tablename__ = "corais"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    localizacao = db.Column(db.String(200), nullable=True)
    especie = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao,
            "especie": self.especie
        }
