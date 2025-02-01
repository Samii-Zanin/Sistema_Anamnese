import customtkinter as ctk

class DadosPessoais(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#c7c7c7",width=1100, height=554)

        # Exemplo de widgets dentro de Dados Pessoais
        #lbl_titulo = ctk.CTkLabel(self, text="Dados Pessoais", font=("Arial", 20))
        #lbl_titulo.pack(pady=10)

        lbl_nome = ctk.CTkLabel(self, text="Nome",text_color="#500138",font=("Arial", 15))
        lbl_nome.place(x=12,y=10)
        entry_nome = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu nome")
        entry_nome.place(x=10,y=30)

        lbl_idade = ctk.CTkLabel(self, text="Idade",text_color="#500138",font=("Arial", 15))
        lbl_idade.place(x=12,y=65)
        entry_idade = ctk.CTkEntry(self, width=300,placeholder_text="Digite sua idade, ex:18")
        entry_idade.place(x=10,y=85)

        # Cidade
        lbl_cidade = ctk.CTkLabel(self, text="Cidade", text_color="#500138", font=("Arial", 15))
        lbl_cidade.place(x=12, y=120)
        entry_cidade = ctk.CTkEntry(self, width=300, placeholder_text="Digite sua cidade, ex: XXXXXXX - XX")
        entry_cidade.place(x=10, y=140)

        # Endereço
        lbl_endereco = ctk.CTkLabel(self, text="Endereço", text_color="#500138", font=("Arial", 15))
        lbl_endereco.place(x=12, y=175)
        entry_endereco = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu endereço, ex: rua, bairro, número")
        entry_endereco.place(x=10, y=195)

        # CEP
        lbl_cep = ctk.CTkLabel(self, text="CEP", text_color="#500138", font=("Arial", 15))
        lbl_cep.place(x=12, y=230)
        entry_cep = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu CEP, ex: XXXXX-XXX")
        entry_cep.place(x=10, y=250)

        # Profissão
        lbl_profissao = ctk.CTkLabel(self, text="Profissão", text_color="#500138", font=("Arial", 15))
        lbl_profissao.place(x=402, y=10)
        entry_profissao = ctk.CTkEntry(self, width=300, placeholder_text="Digite sua profissão")
        entry_profissao.place(x=400, y=30)

        # Estado Civil
        lbl_estado_civil = ctk.CTkLabel(self, text="Estado Civil", text_color="#500138", font=("Arial", 15))
        lbl_estado_civil.place(x=402, y=65)
        entry_estado_civil = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu estado civil")
        entry_estado_civil.place(x=400, y=85)

        # Email
        lbl_email = ctk.CTkLabel(self, text="Email", text_color="#500138", font=("Arial", 15))
        lbl_email.place(x=402, y=120)
        entry_email = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu email, ex: xxxxxxxxxx@gmail.com")
        entry_email.place(x=400, y=140)

        # Celular
        lbl_celular = ctk.CTkLabel(self, text="Celular", text_color="#500138", font=("Arial", 15))
        lbl_celular.place(x=402, y=175)
        entry_celular = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu celular, ex: (xx) xxxxx-xxxx")
        entry_celular.place(x=400, y=195)

        # CPF
        lbl_cpf = ctk.CTkLabel(self, text="CPF", text_color="#500138", font=("Arial", 15))
        lbl_cpf.place(x=402, y=230)
        entry_cpf = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu CPF, ex: xxx.xxx.xxx-xx")
        entry_cpf.place(x=400, y=250)
        


        self.sexo_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        lbl_sexo = ctk.CTkLabel(self, text="Sexo", text_color="#500138", font=("Arial", 15))
        lbl_sexo.place(x=802, y=10)
        # Radio Button para Masculino
        rb_masculino = ctk.CTkRadioButton(
            self, text="Masculino", variable=self.sexo_var, value="Masculino",fg_color="#500138", hover_color="#500138"
        )
        rb_masculino.place(x=800, y=35)

        # Radio Button para Feminino
        rb_feminino = ctk.CTkRadioButton(
            self, text="Feminino", variable=self.sexo_var, value="Feminino",fg_color="#500138", hover_color="#500138"
        )
        rb_feminino.place(x=900, y=35)

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


class Historico(ctk.CTkFrame):
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

class CuidadosQueixas(ctk.CTkFrame):
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

class Avaliacao(ctk.CTkFrame):
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