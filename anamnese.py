import customtkinter as ctk
from tela_inicial import TelaInicial

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Anamneses")
        self.geometry("1100x650")
        self.resizable(False, False)

        # Criar um container para as telas
        self.container = ctk.CTkFrame(self, width=1100, height=650)
        self.container.pack(fill="both", expand=True)

        # Armazenar as instâncias das telas
        self.frames = {}

        # Inicializar com o Painel Inicial
        self.show_frame(TelaInicial)

    def show_frame(self, frame_class):
        # Verificar se a tela já foi criada
        if frame_class not in self.frames:
            frame = frame_class(self.container, self)  # Passa 'self' como controller
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Trazer a tela à frente
        self.frames[frame_class].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
