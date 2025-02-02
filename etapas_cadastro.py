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
    def sim_nao(self,nome_botao,nome_entry,x,y, opcao1, opcao2, opcao3 = None):
        if nome_botao.cget("text") == opcao1:
            nome_botao.configure(text=opcao2, fg_color="red", anchor="e")
            nome_entry.place_forget()
        elif nome_botao.cget("text") == opcao2:
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            nome_entry.place(x=x, y=y)
        elif nome_botao.cget("text") == "Nulo":
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            nome_entry.place(x=x, y=y)
    
    def __init__(self, parent, controller=None):
        super().__init__(parent)
                
        self.controller = controller
        self.parent = parent
        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#c7c7c7",width=1100, height=554)

        lbl_esposicao_sol = ctk.CTkLabel(self, text="Exposição Solar?",text_color="#500138",font=("Arial", 15))
        lbl_esposicao_sol.place(x=12,y=10)
        btn_esposicao_sol = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",  # Cor inicial
            text_color="black",
            hover_color="white",
            corner_radius=8,  # Arredondamento das bordas
            width=80,  # Largura do botão
            height=20,  # Altura do botão
            anchor="center",  # Alinhamento do texto
            command=lambda: self.sim_nao(btn_esposicao_sol,entry_exposicao_sol,10,40,"Sim","Não"),
        )
        btn_esposicao_sol.place(x=225,y=12)
        entry_exposicao_sol = ctk.CTkEntry(self, width=300, placeholder_text="Qual a frequência?")

        lbl_tabagismo = ctk.CTkLabel(self, text="Tabagismo?",text_color="#500138",font=("Arial", 15))
        lbl_tabagismo.place(x=12,y=75)
        btn_tabagismo = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",  # Cor inicial
            text_color="black",
            hover_color="white",
            corner_radius=8,  # Arredondamento das bordas
            width=80,  # Largura do botão
            height=20,  # Altura do botão
            anchor="center",  # Alinhamento do texto
            command=lambda: self.sim_nao(btn_tabagismo,entry_tabagismo,10,105,"Sim","Não"),
        )
        btn_tabagismo.place(x=225,y=77)
        entry_tabagismo = ctk.CTkEntry(self, width=300, placeholder_text="Qual a frequência?")
        
        lbl_alcool = ctk.CTkLabel(self, text="Ingere bebida alcoólica?", text_color="#500138", font=("Arial", 15))
        lbl_alcool.place(x=12, y=140)
        btn_alcool = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",
            text_color="black",
            hover_color="white",
            corner_radius=8,
            width=80,
            height=20,
            anchor="center",
            command=lambda: self.sim_nao(btn_alcool, entry_alcool, 10, 170, "Sim", "Não"),
        )
        btn_alcool.place(x=225, y=142)
        entry_alcool = ctk.CTkEntry(self, width=300, placeholder_text="Qual a frequência?")

        # Prática de atividade física
        lbl_atividade_fisica = ctk.CTkLabel(self, text="Pratica atividade física?", text_color="#500138", font=("Arial", 15))
        lbl_atividade_fisica.place(x=12, y=205)
        btn_atividade_fisica = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",
            text_color="black",
            hover_color="white",
            corner_radius=8,
            width=80,
            height=20,
            anchor="center",
            command=lambda: self.sim_nao(btn_atividade_fisica, entry_atividade_fisica, 10, 235, "Sim", "Não"),
        )
        btn_atividade_fisica.place(x=225, y=207)
        entry_atividade_fisica = ctk.CTkEntry(self, width=300, placeholder_text="Qual a frequência?")

        # Tem filhos
        lbl_filhos = ctk.CTkLabel(self, text="Tem filhos?", text_color="#500138", font=("Arial", 15))
        lbl_filhos.place(x=12, y=270)
        btn_filhos = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",
            text_color="black",
            hover_color="white",
            corner_radius=8,
            width=80,
            height=20,
            anchor="center",
            command=lambda: self.sim_nao(btn_filhos, entry_filhos, 10, 300, "Sim", "Não"),
        )
        btn_filhos.place(x=225, y=272)
        entry_filhos = ctk.CTkEntry(self, width=300, placeholder_text="Quantos?")

        # Uso de medicamento contínuo
        lbl_medicamento = ctk.CTkLabel(self, text="Uso de medicamento contínuo?", text_color="#500138", font=("Arial", 15))
        lbl_medicamento.place(x=12, y=335)
        btn_medicamento = ctk.CTkButton(
            self,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",
            text_color="black",
            hover_color="white",
            corner_radius=8,
            width=80,
            height=20,
            anchor="center",
            command=lambda: self.sim_nao(btn_medicamento, entry_medicamento, 10, 365, "Sim", "Não"),
        )
        btn_medicamento.place(x=225, y=337)
        entry_medicamento = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, qual(is)?")

        lbl_ingestao_agua = ctk.CTkLabel(self, text="Ingestão de Água", text_color="#500138", font=("Arial", 15))
        lbl_ingestao_agua.place(x=402, y=10)
        self.ingestao_agua_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_agua_menos_1 = ctk.CTkRadioButton(
            self, text="-1 Litro", variable=self.ingestao_agua_var, value="-1 Litro",fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_1.place(x=400, y=40)
        rb_agua_menos_2 = ctk.CTkRadioButton(
            self, text="-2 Litros", variable=self.ingestao_agua_var, value="-2 Litros",fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_2.place(x=480, y=40)
        rb_agua_menos_3 = ctk.CTkRadioButton(
            self, text="-3 Litros", variable=self.ingestao_agua_var, value="-3 Litros",fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_3.place(x=560, y=40)
        rb_agua_mais_3 = ctk.CTkRadioButton(
            self, text="+3 Litros", variable=self.ingestao_agua_var, value="+3 Litros",fg_color="#500138", hover_color="#500138"
        )
        rb_agua_mais_3.place(x=640, y=40)

        lbl_qualidade_sono = ctk.CTkLabel(self, text="Qualidade do Sono", text_color="#500138", font=("Arial", 15))
        lbl_qualidade_sono.place(x=402, y=80)
        self.qualidade_sono = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_sono_ruim = ctk.CTkRadioButton(
            self, text="Ruim", variable=self.qualidade_sono, value="Ruim",fg_color="#500138", hover_color="#500138"
        )
        rb_sono_ruim.place(x=400, y=110)
        rb_sono_regular = ctk.CTkRadioButton(
            self, text="Regular", variable=self.qualidade_sono, value="Regular",fg_color="#500138", hover_color="#500138"
        )
        rb_sono_regular.place(x=480, y=110)
        rb_sono_bom = ctk.CTkRadioButton(
            self, text="Boa", variable=self.qualidade_sono, value="Boa",fg_color="#500138", hover_color="#500138"
        )
        rb_sono_bom.place(x=560, y=110)
    
        lbl_horas_sono = ctk.CTkLabel(self, text="Quantas horas/dia:", text_color="#500138", font=("Arial", 15))
        lbl_horas_sono.place(x=402, y=150)
        self.horas_sono_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_sono_menos_6 = ctk.CTkRadioButton(
            self, text="-6H", variable=self.horas_sono_var, value="-6H", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_menos_6.place(x=400, y=180)
        rb_sono_7 = ctk.CTkRadioButton(
            self, text="7H", variable=self.horas_sono_var, value="7H", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_7.place(x=480, y=180)
        rb_sono_8 = ctk.CTkRadioButton(
            self, text="8H", variable=self.horas_sono_var, value="8H", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_8.place(x=560, y=180)
        rb_sono_mais_9 = ctk.CTkRadioButton(
            self, text="+9H", variable=self.horas_sono_var, value="+9H", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_mais_9.place(x=640, y=180)

        # Alimentação
        lbl_alimentacao = ctk.CTkLabel(self, text="Alimentação:", text_color="#500138", font=("Arial", 15))
        lbl_alimentacao.place(x=402, y=220)
        self.alimentacao_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_alimentacao_boa = ctk.CTkRadioButton(
            self, text="Boa", variable=self.alimentacao_var, value="Boa", fg_color="#500138", hover_color="#500138"
        )
        rb_alimentacao_boa.place(x=400, y=250)
        rb_alimentacao_regular = ctk.CTkRadioButton(
            self, text="Regular", variable=self.alimentacao_var, value="Regular", fg_color="#500138", hover_color="#500138"
        )
        rb_alimentacao_regular.place(x=480, y=250)
        rb_alimentacao_pessima = ctk.CTkRadioButton(
            self, text="Péssima", variable=self.alimentacao_var, value="Péssima", fg_color="#500138", hover_color="#500138"
        )
        rb_alimentacao_pessima.place(x=560, y=250)

        # Funcionamento intestinal
        lbl_intestino = ctk.CTkLabel(self, text="Funcionamento intestinal:", text_color="#500138", font=("Arial", 15))
        lbl_intestino.place(x=402, y=290)
        self.intestino_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_intestino_irregular = ctk.CTkRadioButton(
            self, text="Irregular", variable=self.intestino_var, value="Irregular", fg_color="#500138", hover_color="#500138"
        )
        rb_intestino_irregular.place(x=400, y=320)
        rb_intestino_regular = ctk.CTkRadioButton(
            self, text="Regular", variable=self.intestino_var, value="Regular", fg_color="#500138", hover_color="#500138"
        )
        rb_intestino_regular.place(x=480, y=320)

        # Ciclo menstrual
        lbl_ciclo_menstrual = ctk.CTkLabel(self, text="Ciclo menstrual:", text_color="#500138", font=("Arial", 15))
        lbl_ciclo_menstrual.place(x=402, y=360)
        self.ciclo_menstrual_var = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_ciclo_irregular = ctk.CTkRadioButton(
            self, text="Irregular", variable=self.ciclo_menstrual_var, value="Irregular", fg_color="#500138", hover_color="#500138"
        )
        rb_ciclo_irregular.place(x=400, y=390)
        rb_ciclo_regular = ctk.CTkRadioButton(
            self, text="Regular", variable=self.ciclo_menstrual_var, value="Regular", fg_color="#500138", hover_color="#500138"
        )
        rb_ciclo_regular.place(x=480, y=390)
        rb_ciclo_ininterrupto = ctk.CTkRadioButton(
            self, text="Ininterrupto", variable=self.ciclo_menstrual_var, value="Ininterrupto", fg_color="#500138", hover_color="#500138"
        )
        rb_ciclo_ininterrupto.place(x=560, y=390)
        rb_ciclo_menopausa = ctk.CTkRadioButton(
            self, text="Menopausa", variable=self.ciclo_menstrual_var, value="Menopausa", fg_color="#500138", hover_color="#500138"
        )
        rb_ciclo_menopausa.place(x=670, y=390)

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