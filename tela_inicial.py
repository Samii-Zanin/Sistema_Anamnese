import customtkinter as ctk
from PIL import Image
from botao_s_n import Botao

cores = {"rosa forte": "#ad0e86", "rosa claro": "#e97afa"}

class TelaInicial(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        # Configuração do frame principal
        self.configure(width=1100, height=650, fg_color= "#ff85da"
)

        imagem_titulo = ctk.CTkImage(Image.open("imagens\\anamnese2.png"), size=(1200, 800))
        anamnese_txt = ctk.CTkLabel(self, image=imagem_titulo, text="")
        anamnese_txt.place(relx=-0.03, rely=0.05)

        imagem_criar = ctk.CTkImage(Image.open("imagens\\add.png"), size=(250, 200))
        botao_criar = ctk.CTkButton(
            self,
            image=imagem_criar,
            text="",
            compound="top",
            fg_color="#ad0e86",
            hover_color="#ffffff",
            width=250,
            height=200,
            corner_radius=20,
            command=self.ir_para_botoes,
        )
        botao_criar.place(relx=0.2, rely=0.4)

        texto_criar = ctk.CTkLabel(self, text="Criar Anamnese", font=("Arial", 24), text_color="#ffffff")
        texto_criar.place(relx=0.25, rely=0.75)

        imagem_buscar = ctk.CTkImage(Image.open("imagens\\search.png"), size=(250, 200))
        botao_buscar = ctk.CTkButton(
            self,
            image=imagem_buscar,
            text="",
            compound="top",
            fg_color="#ad0e86",
            hover_color="#ffffff",
            width=250,
            height=200,
            corner_radius=20,
        )
        botao_buscar.place(relx=0.6, rely=0.4)

        texto_pesquisar = ctk.CTkLabel(self, text="Pesquisar Paciente", font=("Arial", 24), text_color="#ffffff")
        texto_pesquisar.place(relx=0.64, rely=0.75)

    def ir_para_botoes(self):
        from menu_anamnase import MenuCadastro
        self.controller.show_frame(MenuCadastro)
    def ir_para_pesquisa(self):
        pass
    def ir_para_cadastro(self):
        pass