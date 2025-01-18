import customtkinter as ctk
from PIL import Image
class MenuCadastro(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent
        print(f"controller: {self.controller}, parent: {self.parent}")

        # Configuração do frame principal
        self.configure(width=1100, height=650, fg_color="#ff85da")
        
        
        self.frame_labels_e_entrys = ctk.CTkFrame(self, width=1100, height=554, fg_color="#c7c7c7")
        self.frame_labels_e_entrys.place(x=0, y=97)

        imagem_titulo = ctk.CTkImage(Image.open("imagens\\titulo.png"), size=(270, 39))
        anamnese_txt = ctk.CTkLabel(
            self, 
            image=imagem_titulo, 
            text="",fg_color="#ff85da"
        )
        anamnese_txt.place(relx=0.37, rely=0.01)

        img_dados_pessoais = ctk.CTkImage(Image.open("imagens\\dados.png"), size=(93,43))
        botao_dados_pessoais = ctk.CTkButton(
        self,
        image=img_dados_pessoais,
        text="",
        compound="top",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=93,
        height=43,
        corner_radius=20,
        command=self.ir_para_dados_pessoais
        )
        botao_dados_pessoais.place(relx=0, rely=0.07)

        img_habitos = ctk.CTkImage(Image.open("imagens\\habitos.png"), size=(50,43))
        botao_habitos = ctk.CTkButton(
        self,
        image=img_habitos,
        text="",
        compound="top",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=133,
        height=43,
        corner_radius=20,
        command=self.ir_para_habitos
        )
        botao_habitos.place(relx=0.124, rely=0.07)

        img_historico = ctk.CTkImage(Image.open("imagens\\historicos.png"), size=(58,43))
        botao_historico = ctk.CTkButton(
        self,
        image=img_historico,
        text="",
        compound="top",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=133,
        height=43,
        corner_radius=20,
        )
        botao_historico.place(relx=0.244, rely=0.07)

        img_cuidados_queixas = ctk.CTkImage(Image.open("imagens\\cuidados.png"), size=(90,43))
        botao_cuidado_queixa = ctk.CTkButton(
        self,
        image=img_cuidados_queixas,
        text="",
    
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=140,
        height=43,
        corner_radius=20,
        )
        botao_cuidado_queixa.place(relx=0.364, rely=0.07)
        
        img_avaliacao = ctk.CTkImage(Image.open("imagens\\avaliacao2.png"), size=(50,43))
        botao_avaliacao = ctk.CTkButton(
        self,
        image=img_avaliacao,
        text="",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=133,
        height=43,
        corner_radius=20,
        )
        botao_avaliacao.place(relx=0.49, rely=0.07)

        img_voltar = ctk.CTkImage(Image.open("imagens\\voltar.png"), size=(38,43))
        botao_voltar = ctk.CTkButton(
        self,
        image=img_voltar,
        text="",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=0,
        height=43,
        corner_radius=20,
        )
        botao_voltar.place(x=1020, rely=0.07)

        img_configuracoes = ctk.CTkImage(Image.open("imagens\\configuracoes.png"), size=(38,43))
        botao_configuracoes = ctk.CTkButton(
        self,
        image=img_configuracoes,
        text="",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=0,
        height=43,
        corner_radius=20,
        )
        botao_configuracoes.place(relx=0.853, rely=0.07)



        entry_pesquisa = ctk.CTkEntry(self, placeholder_text="Buscar anamneses", width=189.9, height=51,fg_color="#ff85da",border_color="#ffffff",bg_color="#ff85da",placeholder_text_color="#ffffff",font=("Arial",18), text_color="#ffffff")
        entry_pesquisa.place(relx = 0.61, rely=0.07 )
       
        img_pesquisar = ctk.CTkImage(Image.open("imagens\\search.png"), size=(38,43))
        botao_pesquisar = ctk.CTkButton(
        self,
        image=img_pesquisar,
        text="",
        compound="top",
        fg_color="#ad0e86",
        hover_color="#ffffff",
        width=0,
        height=43,
        corner_radius=20,
        )
        botao_pesquisar.place(relx=0.780, rely=0.07)
    def ir_para_dados_pessoais(self):
        from etapas_cadastro import DadosPessoais
        for widget in self.frame_labels_e_entrys.winfo_children():
            widget.destroy()
        dados_pessoais = DadosPessoais(self.frame_labels_e_entrys, self.controller)
        dados_pessoais.place(x=0,y=0)
    def ir_para_habitos(self):
        from etapas_cadastro import Habitos
        for widget in self.frame_labels_e_entrys.winfo_children():
            widget.destroy()
        habitos = Habitos(self.frame_labels_e_entrys, self.controller)
        habitos.place(x=0,y=0)
# Testando diretamente a classe MenuCadastro
if __name__ == "__main__":
    # Criar a janela principal temporária
    app = ctk.CTk()  # Inicializa o CustomTkinter
    app.title("Teste MenuCadastro")
    app.geometry("1100x650")

    # Instanciar o MenuCadastro diretamente
    menu_cadastro = MenuCadastro(app)  # Passa 'app' como parent
    menu_cadastro.pack(fill="both", expand=True)  # Exibe o frame no container

    # Executar o mainloop
    app.mainloop()
