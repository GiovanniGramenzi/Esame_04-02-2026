import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def popola_dd_roles(self):
        roles = self._model.roles
        for role in roles:
            self._view.dd_ruolo.options.append(ft.dropdown.Option(role))
        self._view.update()
    def handle_crea_grafo(self, e):
        self._view.list_risultato.controls.clear()
        role=str(self._view.dd_ruolo.value)
        self._model.build_graph(role)
        n=self._model.get_number_of_nodes()
        a=self._model.get_number_of_edges()
        self._view.list_risultato.controls.append(ft.Text(f'Nodi:{n},Archi:{a}'))
        self._view.btn_classifica.disabled = False
        self._view.btn_cerca_percorso.disabled = False
        self._view.update()



    def handle_classifica(self, e):
        classifica=self._model.classifica()
        self._view.list_risultato.controls.clear()
        for i in classifica:
            self._view.list_risultato.controls.append(ft.Text(f'{i[0]} -->delta:{i[1]}'))
        self._view.update()

