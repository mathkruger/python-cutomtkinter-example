import customtkinter as TK

class WindowBase(TK.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.widgets = {}
    
    def create_panel(self, name, master, padx=10, pady=10, fill="both", expand=True):
        self.widgets[name] = TK.CTkFrame(master=master)
        self.widgets[name].pack(pady=pady, padx=padx, fill=fill, expand=expand)
        return self.get_widget(name)

    def create_label(self, name, master, text, padx=10, pady=10):
        self.widgets[name] = TK.CTkLabel(master=master, text=text)
        self.widgets[name].pack(pady=pady, padx=padx)
    
    def create_entry(self, name, master, padx=10, pady=10):
        self.widgets[name] = TK.CTkEntry(master=master)
        self.widgets[name].pack(pady=pady, padx=padx)

    def create_button(self, name, master, text, command, padx=10, pady=10):
        self.widgets[name] = TK.CTkButton(
            master=master,
            text=text,
            command=command
        )
        self.widgets[name].pack(pady=pady, padx=padx)
    
    def get_widget(self, name):
        return self.widgets[name]