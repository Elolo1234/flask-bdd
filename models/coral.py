class Coral:
    def __init__(self, id, especie, nome_popular, extincao, indice_temperatura, indice_poluicao):
        self.id = id
        self.especie = especie
        self.nome_popular = nome_popular
        self.extincao = extincao
        self.indice_temperatura = indice_temperatura
        self.indice_poluicao = indice_poluicao

    def to_dict(self):
        return{
            "id": self.id,
            "especie" : self.especie,
            "nome_popular" : self.nome_popular,
            "extincao" : self.extincao,
            "indice_temperatura" : self.indice_temperatura,
            "indice_poluicao" : self.indice_poluicao
        }