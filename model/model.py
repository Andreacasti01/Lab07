from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self.lista_bib = []
        self.lista_lib = []

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        lista_filtrata = []
        nessun_filtro_biblioteca = (biblioteca == "Nessun filtro")
        nessun_filtro_genere = (genere == "Nessun filtro")
        if nessun_filtro_biblioteca and nessun_filtro_genere:
            for l in self.lista_lib:
                lista_filtrata.append(l)
            return lista_filtrata
        elif nessun_filtro_biblioteca and not nessun_filtro_genere:
            for l in self.lista_lib:
                if l.genere == genere:
                    lista_filtrata.append(l)
            return lista_filtrata
        elif not nessun_filtro_biblioteca and nessun_filtro_genere:
            for b in self.lista_bib:
                if b.nome == biblioteca:
                    for l in self.lista_lib:
                        if l.id_biblioteca==b.id:
                            lista_filtrata.append(l)
            return lista_filtrata
        else:
            for b in self.lista_bib:
                if b.nome == biblioteca:
                    for l in self.lista_lib:
                        if l.id_biblioteca==b.id and l.genere==genere:
                            lista_filtrata.append(l)
            return lista_filtrata

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        self.lista_lib = self._libro_dao.read_libro_from_db()
        lista_genere = []
        for libro in self.lista_lib:
            if libro.genere in lista_genere:
                pass
            else:
                lista_genere.append(libro.genere)
        return lista_genere

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        self.lista_bib = self._biblioteca_dao.read_biblioteche_from_db()
        return self.lista_bib