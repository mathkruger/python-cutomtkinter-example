from views.base.WindowBase import WindowBase
from controllers.MainController import MainController

class MainView(WindowBase):
    def __init__(self) -> None:
        super().__init__()

        self.title = "Calculador de Média"
        self.minsize(width=600, height=500)

        self.controller = MainController(self)

        self.create_ui()
    
    def create_ui(self):
        self.create_form()
        self.create_label("lbl_resultado", self, "")
        self.create_button("btn_media", self, "Calcular", self.controller.show_results)
    
    def create_form(self):    
        form = self.create_panel("formulario", self, 10, 10)

        self.create_label("lbl_portugues", form, "Média Português", pady=0)
        self.create_entry("media_portugues", form)
        
        self.create_label("lbl_matematica", form, "Média Matemática", pady=0)
        self.create_entry("media_matematica", form)

        self.create_label("lbl_ciencias", form, "Média Ciências", pady=0)
        self.create_entry("media_ciencias", form)

        self.create_label("lbl_historia", form, "Média História", pady=0)
        self.create_entry("media_historia", form)

        self.create_label("lbl_geografia", form, "Média Geografia", pady=0)
        self.create_entry("media_geografia", form)