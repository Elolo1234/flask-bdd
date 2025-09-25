import json
import os


CAMINHO_CORAL_JSON = os.path.join(os.path.dirname(__file__), "..", "dados", "corais.json")


def inicializar_arquivo():
    os.makedirs(os.path.dirname(CAMINHO_CORAL_JSON), exist_ok=True)
    if not os.path.exists(CAMINHO_CORAL_JSON):
        with open(CAMINHO_CORAL_JSON, "w", encoding="utf-8") as f:
            json.dump([], f)

def carregar_corais_json():
    inicializar_arquivo()
    try:
        with open(CAMINHO_CORAL_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []

def salvar_corais_json(lista_corais):

    with open(CAMINHO_CORAL_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_corais, f, indent=4, ensure_ascii=False)

def adicionar_coral_json(coral):

    corais = carregar_corais_json()
    coral["id"] = len(corais) + 1
    corais.append(coral)
    salvar_corais_json(corais)
    return coral

def listar_corais_json():

    return carregar_corais_json()

def buscar_coral_por_id_json(id):

    corais = carregar_corais_json()
    for coral in corais:
        if coral["id"] == id:
            return coral
    return None

def deletar_coral_por_id_json(id):
    
    corais = carregar_corais_json()
    coral_encontrado = None
    nova_lista = []

    for coral in corais:
        if coral["id"] == id:
            coral_encontrado = coral
        else:
            nova_lista.append(coral)

    if coral_encontrado:
        salvar_corais_json(nova_lista)
        return True  
    else:
        return False

def atualizar_coral_por_id_json(id, novos_dados):
    corais = carregar_corais_json()
    coral_atualizado = None

    for coral in corais:
        if coral["id"] == id:
            coral.update(novos_dados)
            coral_atualizado = coral
            break

    if coral_atualizado:
        salvar_corais_json(corais)
        return coral_atualizado
    else:
        return None
