from services.GradesService import GradesService


class MainController():
    def __init__(self, ui) -> None:
        self.ui = ui
        self.service = GradesService()
    
    def get_grades(self):
        return [
            float(self.ui.get_widget("media_portugues").get()),
            float(self.ui.get_widget("media_matematica").get()),
            float(self.ui.get_widget("media_ciencias").get()),
            float(self.ui.get_widget("media_historia").get()),
            float(self.ui.get_widget("media_geografia").get())
        ]

    def show_results(self):
        grades = self.get_grades()
        avg = self.service.get_avarage(grades)
        points_to_add = self.service.get_points_to_add(avg)
        
        self.ui.get_widget("lbl_resultado").configure(text=f"Sua média é: {avg}.\nPontos a adicionar para sua casa: {points_to_add}")