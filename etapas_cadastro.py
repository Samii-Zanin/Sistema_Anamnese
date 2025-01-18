import customtkinter as ctk

class DadosPessoais(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#c7c7c7",width=1100, height=554)

        # Exemplo de widgets dentro de Dados Pessoais
        lbl_titulo = ctk.CTkLabel(self, text="Dados Pessoais", font=("Arial", 20))
        lbl_titulo.pack(pady=10)

        lbl_nome = ctk.CTkLabel(self, text="Nome:")
        lbl_nome.pack(pady=5)

        entry_nome = ctk.CTkEntry(self, width=300)
        entry_nome.pack(pady=5)

        lbl_idade = ctk.CTkLabel(self, text="Idade:")
        lbl_idade.pack(pady=5)

        entry_idade = ctk.CTkEntry(self, width=300)
        entry_idade.pack(pady=5)

class Habitos(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#c7c7c7",width=1100, height=554)

        # Exemplo de widgets dentro de Dados Pessoais
        lbl_titulo = ctk.CTkLabel(self, text="Hábitos", font=("Arial", 20))
        lbl_titulo.pack(pady=10)

        lbl_nome = ctk.CTkLabel(self, text="Nome:")
        lbl_nome.pack(pady=5)

        entry_nome = ctk.CTkEntry(self, width=300)
        entry_nome.pack(pady=5)

        lbl_idade = ctk.CTkLabel(self, text="Idade:")
        lbl_idade.pack(pady=5)

        entry_idade = ctk.CTkEntry(self, width=300)
        entry_idade.pack(pady=5)

