import json
import os

CAMINHO_PESQUISADOR_JSON = os.path.join(os.path.dirname(__file__), '..', 'dados', 'pesquisadores.json')

def inicializar_arquivo():
    os.makedirs(os.path.dirname(CAMINHO_PESQUISADOR_JSON), exist_ok=True)
    if not os.path.exists(CAMINHO_PESQUISADOR_JSON):
        with open(CAMINHO_PESQUISADOR_JSON, "w", encoding="utf-8") as f:
            json.dump([], f)

def carregar_pesquisadores_json():
    inicializar_arquivo()
    try:
        with open(CAMINHO_PESQUISADOR_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []

def salvar_pesquisadores_json(lista_pesquisadores):

    with open(CAMINHO_PESQUISADOR_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_pesquisadores, f, indent=4, ensure_ascii=False)

def adicionar_pesquisador_json(pesquisador):

    pesquisadores = carregar_pesquisadores_json()
    pesquisador["id"] = len(pesquisadores) + 1
    pesquisadores.append(pesquisador)
    salvar_pesquisadores_json(pesquisadores)
    return pesquisador

def listar_pesquisadores_json():

    return carregar_pesquisadores_json()

def buscar_pesquisador_por_id_json(id):
    pesquisadores = carregar_pesquisadores_json()
    for p in pesquisadores:
        if p["id"] == id:
            return p
    return None

def atualizar_pesquisador_json(id, dados_atualizados):

    pesquisadores = carregar_pesquisadores_json()
    for i, p in enumerate(pesquisadores):
        if p["id"] == id:
            pesquisadores[i].update(dados_atualizados)
            salvar_pesquisadores_json(pesquisadores)
            return pesquisadores[i]
    return None

def deletar_pesquisador_por_id_json(id):
    
    pesquisadores = carregar_pesquisadores_json()
    nova_lista = [p for p in pesquisadores if p["id"] != id]
    if len(nova_lista) < len(pesquisadores):
        salvar_pesquisadores_json(nova_lista)
        return True
    return False
