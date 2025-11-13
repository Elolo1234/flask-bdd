from extensions import db

class Pesquisa(db.Model):
    __tablename__ = "pesquisas"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    objetivo = db.Column(db.String(300))
    ano = db.Column(db.Integer)
    local = db.Column(db.String(200))
    pesquisador_id = db.Column(db.Integer, db.ForeignKey("pesquisadores.id"))
    coral_id = db.Column(db.Integer, db.ForeignKey("corais.id"))

    pesquisador = db.relationship("models.pesquisador.Pesquisador")
    coral = db.relationship("models.coral.Coral")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "objetivo": self.objetivo,
            "ano": self.ano,
            "local": self.local,
            "pesquisador_id": self.pesquisador_id,
            "coral_id": self.coral_id,
        }
