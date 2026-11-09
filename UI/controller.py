import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        lista_biblioteche = self._model.get_biblioteche()
        self._view.drop_biblioteche.options.clear()
        self._view.drop_biblioteche.options.append(ft.dropdown.Option("Nessun filtro"))
        for bib in lista_biblioteche:
            self._view.drop_biblioteche.options.append(ft.dropdown.Option(bib.nome))
        lista_generi = self._model.get_generi()
        self._view.drop_genere.options.clear()
        self._view.drop_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in lista_generi:
            self._view.drop_genere.options.append(ft.dropdown.Option(g))

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
    def filtra_libri(self, e):
        biblio_selected = self._view.drop_biblioteche.value
        genere_selected = self._view.drop_genere.value
        self._view.libri_filtrati.controls.clear()
        lista_libri_filtrati = self._model.get_libri_filtrati(biblio_selected, genere_selected)
        if len(lista_libri_filtrati) == 0:
            self._view.show_alert("Nessun libro disponibile")
        else:
            for l in lista_libri_filtrati:
                libro = ft.Text(value=f"'{l.titolo}' scritto da {l.autore}")
                self._view.libri_filtrati.controls.append(libro)
                self._view.libri_filtrati.update()
