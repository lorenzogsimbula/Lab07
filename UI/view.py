import flet as ft
from flet.core.dropdown import Dropdown


from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._dd_musei=ft.Dropdown(editable= False,
                                    label="Museo",
                                    width=300,
                                    options=self.controller.popola_dd_museo()+[ft.DropdownOption("Nessun Filtro")]
                                   )


        self._dd_epoche=ft.Dropdown(editable=False,
                                    label="Epoca",
                                    width=200,
                                    options=self.controller.popola_dd_epoca() + [ft.DropdownOption("Nessun Filtro")],

                                    )

        self.row = ft.Row([self._dd_musei, self._dd_epoche],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=20
                          )

        # Sezione 3: Artefatti
        # TODO
        self.lv_artefatti=ft.ListView(expand=True,spacing=10,padding=20)
        self.btn_artefatti=ft.ElevatedButton(text="Mostra artefatti",
                                            on_click=self.controller.mostra_artefatti
                                             )
        self.row2 = ft.Row(controls=[self.btn_artefatti],
                           alignment=ft.MainAxisAlignment.CENTER)
        self.row3 = ft.Row(controls=[self.lv_artefatti],
                           alignment=ft.MainAxisAlignment.CENTER)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            self.row,
            ft.Divider(),

            # Sezione 3: Artefatti
            # TODO
            self.row2,
            self.row3

        )

        self.page.scroll = "adaptive"
        self.page.update()


    def cambia_tema(self,e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
