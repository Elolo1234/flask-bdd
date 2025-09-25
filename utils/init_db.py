
from dao.coral_dao import CoralDAO
from dao.pesquisador_dao import PesquisadorDAO
from dao.pesquisa_dao import PesquisaDAO

def init_db():
    """Inicializa todas as tabelas do banco"""
    CoralDAO().create_table()
    PesquisadorDAO().create_table()
    PesquisaDAO().create_table()
