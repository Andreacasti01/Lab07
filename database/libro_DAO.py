from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def read_libro_from_db(self):
        cnx = DBConnect.get_connection(nome_pool="mio_pool", dimensione_pool=3)
        if cnx is not None:
            query = "SELECT * FROM `libro`"
            cursor = cnx.cursor()
            cursor.execute(query)
            result=[]
            for row in cursor:
                libro=Libro(*row)
                result.append(libro)
            cursor.close()
            cnx.close()
            return result
        else:
            return None