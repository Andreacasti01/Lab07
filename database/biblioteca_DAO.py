from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def read_biblioteche_from_db(self):
        cnx = DBConnect.get_connection(nome_pool="mio_pool", dimensione_pool=3)
        if cnx is not None:
            #print("Connessione effettuata")
            query = "SELECT * FROM `biblioteca`"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Nessuna connessione")
            return None
