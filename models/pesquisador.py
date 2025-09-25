class Pesquisador:
    def __init__(self, id, nome, instituicao, especialidade, email):
        self.id = id
        self.nome = nome
        self.instituicao = instituicao
        self.especialidade = especialidade
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "instituicao": self.instituicao,
            "especialidade": self.especialidade,
            "email": self.email
        }
