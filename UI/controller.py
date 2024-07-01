import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.grafo.number_of_nodes()}, "
                                                      f"Numero di archi: {self._model.grafo.number_of_edges()}"))
        self._view.txt_result.controls.append(ft.Text(f"Max: {self._model.Max}, "
                                                      f"Min: {self._model.Min}"))

        self._view.update_page()

    def handle_countedges(self, e):
        soglia = self._view.txt_name.value
        try:
            s = float(soglia)
        except:
            self._view.create_alert("inserire un numero, (per decimali usare il punto e non la virgola)")
            return
        if s < self._model.Min or s > self._model.Max:
            self._view.create_alert("Inserire un numero compreso tra max e min")
            return
        else:
            sotto,sopra = self._model.sottoOsopra(s)
            self._view.txt_result2.controls.append(ft.Text(f"sopra s: {sopra}; "
                                                          f"sotto s: {sotto}"))
        self._view.update_page()

    def handle_search(self, e):
        soglia = self._view.txt_name.value
        try:
            s = float(soglia)
        except:
            self._view.create_alert("inserire un numero, (per decimali usare il punto e non la virgola)")
            return
        if s < self._model.Min or s > self._model.Max:
            self._view.create_alert("Inserire un numero compreso tra max e min")
            return
        else:
            self._model.sottoOsopra(s)
        peso,percorso = self._model.cercaPercorso()
        self._view.txt_result3.controls.append(ft.Text(f"Peso massimo: {peso}"))
        for arco in percorso:
            self._view.txt_result3.controls.append(ft.Text(f"{arco[0]} --> {arco[1]},"
                                                           f" peso {arco[2]["weight"]}"))
        self._view.update_page()




