import flet as ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model,alert: AlertManager):
        self._model = model
        self._view = view
        self._alert = alert

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_museo(self):
        options=[]
        lista_musei=self._model.get_lista_musei()

        for museo in lista_musei :
            options.append(ft.DropdownOption(museo.nome))
        return options
    def popola_dd_epoca(self):
        options=[]
        lista_epoche=self._model.get_lista_epoche()

        for epoca in lista_epoche :
            options.append(ft.DropdownOption(epoca))
        return options


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):
        self.museo_selezionato = self._view._dd_musei.value
        self.epoca_selezionata= self._view._dd_epoche.value

        if self._view._dd_musei.value is None and self._view._dd_epoche.value is None:
            raise Exception(self._alert.show_alert('museo ed epoca non selezionati'))
        elif self._view._dd_epoche.value is None:
            raise Exception(self._alert.show_alert('epoca non selezionata'))
        elif self._view._dd_musei.value is None:
            raise Exception(self._alert.show_alert('museo non selezionato'))

        artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)
        print(artefatti)
        self._view.lv_artefatti.clean()

        for artefatto in artefatti :
            self._view.lv_artefatti.controls.append(ft.Text(artefatto))
        print(artefatti)
        if len(self._view.lv_artefatti.controls) == 0 :
            self._alert.show_alert("Nessun artefatto trovato")
        self._view.update()
