import customtkinter as ctk

class DadosPessoais(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#ff85da", width=1100, height=554)

        # Exemplo de widgets dentro de Dados Pessoais
        lbl_nome = ctk.CTkLabel(self, text="Nome", text_color="#500138", font=("Arial", 15))
        lbl_nome.place(x=12, y=10)
        entry_nome = ctk.CTkEntry(self, width=300, placeholder_text="Digite seu nome")
        entry_nome.place(x=10, y=30)

        lbl_idade = ctk.CTkLabel(self, text="Idade", text_color="#500138", font=("Arial", 15))
        lbl_idade.place(x=12, y=65)
        entry_idade = ctk.CTkEntry(self, width=300, placeholder_text="Digite sua idade, ex:18")
        entry_idade.place(x=10, y=85)

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
            self, text="Masculino", variable=self.sexo_var, value="Masculino", fg_color="#500138", hover_color="#500138"
        )
        rb_masculino.place(x=800, y=35)

        # Radio Button para Feminino
        rb_feminino = ctk.CTkRadioButton(
            self, text="Feminino", variable=self.sexo_var, value="Feminino", fg_color="#500138", hover_color="#500138"
        )
        rb_feminino.place(x=900, y=35)

        # Botão "Próximo"
        btn_proximo = ctk.CTkButton(
            self,
            text="Próximo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#500138",
            hover_color="#ffffff",
            corner_radius=8,
            width=100,
            height=30,
            command=self.ir_para_habitos,
        )
        btn_proximo.place(x=980, y=500)

    def ir_para_habitos(self):
        if self.controller:
            self.controller.atualizar_frame(Habitos)


class Habitos(ctk.CTkFrame):
    def sim_nao(self, nome_botao, nome_entry, x, y, opcao1, opcao2, opcao3=None):
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
        self.configure(fg_color="#ff85da", width=1100, height=554)

        lbl_esposicao_sol = ctk.CTkLabel(self, text="Exposição Solar?", text_color="#500138", font=("Arial", 15))
        lbl_esposicao_sol.place(x=12, y=10)
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
            command=lambda: self.sim_nao(btn_esposicao_sol, entry_exposicao_sol, 10, 40, "Sim", "Não"),
        )
        btn_esposicao_sol.place(x=225, y=12)
        entry_exposicao_sol = ctk.CTkEntry(self, width=300, placeholder_text="Qual a frequência?")

        lbl_tabagismo = ctk.CTkLabel(self, text="Tabagismo?", text_color="#500138", font=("Arial", 15))
        lbl_tabagismo.place(x=12, y=75)
        btn_tabagismo = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_tabagismo, entry_tabagismo, 10, 105, "Sim", "Não"),
        )
        btn_tabagismo.place(x=225, y=77)
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
        lbl_medicamento.place(x=12, y=337)
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
            self, text="-1 Litro", variable=self.ingestao_agua_var, value="-1 Litro", fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_1.place(x=400, y=40)
        rb_agua_menos_2 = ctk.CTkRadioButton(
            self, text="-2 Litros", variable=self.ingestao_agua_var, value="-2 Litros", fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_2.place(x=480, y=40)
        rb_agua_menos_3 = ctk.CTkRadioButton(
            self, text="-3 Litros", variable=self.ingestao_agua_var, value="-3 Litros", fg_color="#500138", hover_color="#500138"
        )
        rb_agua_menos_3.place(x=560, y=40)
        rb_agua_mais_3 = ctk.CTkRadioButton(
            self, text="+3 Litros", variable=self.ingestao_agua_var, value="+3 Litros", fg_color="#500138", hover_color="#500138"
        )
        rb_agua_mais_3.place(x=640, y=40)

        lbl_qualidade_sono = ctk.CTkLabel(self, text="Qualidade do Sono", text_color="#500138", font=("Arial", 15))
        lbl_qualidade_sono.place(x=402, y=80)
        self.qualidade_sono = ctk.StringVar(value="")  # Variável para armazenar a escolha
        rb_sono_ruim = ctk.CTkRadioButton(
            self, text="Ruim", variable=self.qualidade_sono, value="Ruim", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_ruim.place(x=400, y=110)
        rb_sono_regular = ctk.CTkRadioButton(
            self, text="Regular", variable=self.qualidade_sono, value="Regular", fg_color="#500138", hover_color="#500138"
        )
        rb_sono_regular.place(x=480, y=110)
        rb_sono_bom = ctk.CTkRadioButton(
            self, text="Boa", variable=self.qualidade_sono, value="Boa", fg_color="#500138", hover_color="#500138"
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

        # Botão "Próximo"
        btn_proximo = ctk.CTkButton(
            self,
            text="Próximo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#500138",
            hover_color="#ffffff",
            corner_radius=8,
            width=100,
            height=30,
            command=self.ir_para_historico,
        )
        btn_proximo.place(x=980, y=500)

    def ir_para_historico(self):
        if self.controller:
            self.controller.atualizar_frame(Historico)


class Historico(ctk.CTkFrame):
    def sim_nao(self, nome_botao, nome_entry, x, y, opcao1, opcao2, opcao3=None):
        if nome_botao.cget("text") == opcao1:
            nome_botao.configure(text=opcao2, fg_color="red", anchor="e")
            if nome_entry and x and y != None:
                nome_entry.place_forget()
        elif nome_botao.cget("text") == opcao2:
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
        elif nome_botao.cget("text") == "Nulo":
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        self.configure(fg_color="#ff85da", width=1100, height=554)

        lbl_hist_clinico = ctk.CTkLabel(self, text="Histórico Clínico", text_color="#500138", font=("Arial", 25))
        lbl_hist_clinico.place(x=10,y=10)

        lbl_alergia = ctk.CTkLabel(self, text="Uso de medicamento contínuo?", text_color="#500138", font=("Arial", 15))
        lbl_alergia.place(x=12, y=45)
        btn_alergia = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_alergia, entry_alergia, 10, 75, "Sim", "Não"),
        )
        btn_alergia.place(x=225, y=47)
        entry_alergia = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, qual(is)?")    

        lbl_gestante = ctk.CTkLabel(self, text="É gestante?", text_color="#500138", font=("Arial", 15))
        lbl_gestante.place(x=12, y=105)
        btn_gestante= ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_gestante, None, None, None, "Sim", "Não"),
        )
        btn_gestante.place(x=225, y=105)
        
        lbl_lactose = ctk.CTkLabel(self, text="Intolerância à lactose?", text_color="#500138", font=("Arial", 15))
        lbl_lactose.place(x=12, y=130)
        btn_lactose = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_lactose, None, None, None, "Sim", "Não"),
        )
        btn_lactose.place(x=225, y=130)

        # Diabetes
        lbl_diabetes = ctk.CTkLabel(self, text="Diabetes:", text_color="#500138", font=("Arial", 15))
        lbl_diabetes.place(x=12, y=155)
        btn_diabetes = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_diabetes, entry_diabetes, 10, 180, "Sim", "Não"),
        )
        btn_diabetes.place(x=225, y=155)
        entry_diabetes = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, qual tipo?")

        # Doença cardiorrespiratória
        lbl_cardio = ctk.CTkLabel(self, text="Doença cardiorrespiratória?", text_color="#500138", font=("Arial", 15))
        lbl_cardio.place(x=12, y=210)
        btn_cardio = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_cardio, None, None, None, "Sim", "Não"),
        )
        btn_cardio.place(x=225, y=210)

        # Trombose
        lbl_trombose = ctk.CTkLabel(self, text="Trombose:", text_color="#500138", font=("Arial", 15))
        lbl_trombose.place(x=12, y=235)
        btn_trombose = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_trombose, None, None, None, "Sim", "Não"),
        )
        btn_trombose.place(x=225, y=235)

        # Hipertireoidismo
        lbl_hipertireoidismo = ctk.CTkLabel(self, text="Hipertireoidismo:", text_color="#500138", font=("Arial", 15))
        lbl_hipertireoidismo.place(x=12, y=260)
        btn_hipertireoidismo = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_hipertireoidismo, None, None, None, "Sim", "Não"),
        )
        btn_hipertireoidismo.place(x=225, y=260)

        # Hipotireoidismo
        lbl_hipotireoidismo = ctk.CTkLabel(self, text="Hipotireoidismo:", text_color="#500138", font=("Arial", 15))
        lbl_hipotireoidismo.place(x=12, y=285)
        btn_hipotireoidismo = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_hipotireoidismo, None, None, None, "Sim", "Não"),
        )
        btn_hipotireoidismo.place(x=225, y=285)

        # Insuficiência Renal
        lbl_renal = ctk.CTkLabel(self, text="Insuficiência Renal:", text_color="#500138", font=("Arial", 15))
        lbl_renal.place(x=12, y=310)
        btn_renal = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_renal, None, None, None, "Sim", "Não"),
        )
        btn_renal.place(x=225, y=310)

        # Colesterol
        lbl_colesterol = ctk.CTkLabel(self, text="Colesterol:", text_color="#500138", font=("Arial", 15))
        lbl_colesterol.place(x=12, y=335)
        btn_colesterol = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_colesterol, None, None, None, "Sim", "Não"),
        )
        btn_colesterol.place(x=225, y=335)

        # Triglicerídeos
        lbl_triglicerideos = ctk.CTkLabel(self, text="Triglicerídeos:", text_color="#500138", font=("Arial", 15))
        lbl_triglicerideos.place(x=12, y=360)
        btn_triglicerideos = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_triglicerideos, None, None, None, "Sim", "Não"),
        )
        btn_triglicerideos.place(x=225, y=360)

        # Epilepsia-convulsões
        lbl_epilepsia = ctk.CTkLabel(self, text="Epilepsia-convulsões:", text_color="#500138", font=("Arial", 15))
        lbl_epilepsia.place(x=12, y=385)
        btn_epilepsia = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_epilepsia, None, None, None, "Sim", "Não"),
        )
        btn_epilepsia.place(x=225, y=385)

        # Histórico oncológico
        lbl_oncologico = ctk.CTkLabel(self, text="Histórico oncológico:", text_color="#500138", font=("Arial", 15))
        lbl_oncologico.place(x=12, y=410)
        btn_oncologico = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_oncologico, None, None, None, "Sim", "Não"),
        )
        btn_oncologico.place(x=225, y=410)

        # Hipertensão arterial
        lbl_hipertensao = ctk.CTkLabel(self, text="Hipertensão arterial:", text_color="#500138", font=("Arial", 15))
        lbl_hipertensao.place(x=12, y=435)
        btn_hipertensao = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_hipertensao, None, None, None, "Sim", "Não"),
        )
        btn_hipertensao.place(x=225, y=435)

        # Hipotensão arterial
        lbl_hipotensao = ctk.CTkLabel(self, text="Hipotensão arterial:", text_color="#500138", font=("Arial", 15))
        lbl_hipotensao.place(x=12, y=460)
        btn_hipotensao = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_hipotensao, None, None, None, "Sim", "Não"),
        )
        btn_hipotensao.place(x=225, y=460)

        # Portador de marcapasso
        lbl_marcapasso = ctk.CTkLabel(self, text="Portador de marcapasso?", text_color="#500138", font=("Arial", 15))
        lbl_marcapasso.place(x=12, y=485)
        btn_marcapasso = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_marcapasso, None, None, None, "Sim", "Não"),
        )
        btn_marcapasso.place(x=225, y=485)

        #HISTÓRICO FAMILIAR
        lbl_hist_familiar = ctk.CTkLabel(self, text="Histórico Familiar", text_color="#500138", font=("Arial", 25))
        lbl_hist_familiar.place(x=420,y=10)

        lbl_colesterol_alto = ctk.CTkLabel(self, text="Colesterol Alto?", text_color="#500138", font=("Arial", 15))
        lbl_colesterol_alto.place(x=422, y=45)
        btn_colesterol_alto = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_colesterol_alto, entry_colesterol_alto, 420, 75, "Sim", "Não"),
        )
        btn_colesterol_alto.place(x=635, y=47)
        entry_colesterol_alto = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")    

        lbl_hipo_hipertensao = ctk.CTkLabel(self, text="Hipo/Hipertensão arterial?", text_color="#500138", font=("Arial", 15))
        lbl_hipo_hipertensao.place(x=422, y=105)
        btn_hipo_hipertensao= ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_hipo_hipertensao, entry_hipo_hipertensao, 420, 135, "Sim", "Não"),
        )
        btn_hipo_hipertensao.place(x=635, y=105)
        entry_hipo_hipertensao = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")

        lbl_cardiovasculares = ctk.CTkLabel(self, text="Doenças cardiovasculares?", text_color="#500138", font=("Arial", 15))
        lbl_cardiovasculares.place(x=422, y=165)
        btn_cardiovasculares = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_cardiovasculares, entry_cardiovasculares, 420, 195, "Sim", "Não"),
        )
        btn_cardiovasculares.place(x=635, y=165)
        entry_cardiovasculares = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")
        

        # Históricos oncológicos
        lbl_oncologicos = ctk.CTkLabel(self, text="Históricos oncológicos?", text_color="#500138", font=("Arial", 15))
        lbl_oncologicos.place(x=422, y=225)
        btn_oncologicos = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_oncologicos, entry_oncologicos, 420, 255, "Sim", "Não"),
        )
        btn_oncologicos.place(x=635, y=225)
        entry_oncologicos = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")
        

        # Diabetes
        lbl_diabetes = ctk.CTkLabel(self, text="Diabetes?", text_color="#500138", font=("Arial", 15))
        lbl_diabetes.place(x=422, y=285)
        btn_diabetes = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_diabetes, entry_diabetes, 420, 315, "Sim", "Não"),
        )
        btn_diabetes.place(x=635, y=285)
        entry_diabetes = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")
       

        # Doença cardiorrespiratória
        lbl_cardiorrespiratoria = ctk.CTkLabel(self, text="Doença cardiorrespiratória?", text_color="#500138", font=("Arial", 15))
        lbl_cardiorrespiratoria.place(x=422, y=345)
        btn_cardiorrespiratoria = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_cardiorrespiratoria, entry_cardiorrespiratoria, 420, 375, "Sim", "Não"),
        )
        btn_cardiorrespiratoria.place(x=635, y=345)
        entry_cardiorrespiratoria = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")
        

        # Obesidade
        lbl_obesidade = ctk.CTkLabel(self, text="Obesidade?", text_color="#500138", font=("Arial", 15))
        lbl_obesidade.place(x=422, y=405)
        btn_obesidade = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_obesidade, entry_obesidade, 420, 435, "Sim", "Não"),
        )
        btn_obesidade.place(x=635, y=405)
        entry_obesidade = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, quem?")

        btn_proximo = ctk.CTkButton(
            self,
            text="Próximo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#500138",
            hover_color="#ffffff",
            corner_radius=8,
            width=100,
            height=30,
            command=self.ir_para_cuidados_queixas,
        )
        btn_proximo.place(x=980, y=500)



    def ir_para_cuidados_queixas(self):
        if self.controller:
            self.controller.atualizar_frame(CuidadosQueixas)


class CuidadosQueixas(ctk.CTkFrame):
    def sim_nao(self, nome_botao, nome_entry, x, y, opcao1, opcao2, opcao3=None):
        if nome_botao.cget("text") == opcao1:
            nome_botao.configure(text=opcao2, fg_color="red", anchor="e")
            if nome_entry and x and y != None:
                nome_entry.place_forget()
        elif nome_botao.cget("text") == opcao2:
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
        elif nome_botao.cget("text") == "Nulo":
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#ff85da", width=1100, height=554)

        # Exemplo de widgets dentro de Dados Pessoais
        lbl_cuidados = ctk.CTkLabel(self, text="Cuidados", text_color="#500138", font=("Arial", 25))
        lbl_cuidados.place(x=10,y=10)

        lbl_filtro_solar = ctk.CTkLabel(self, text="Utiliza filtro solar?", text_color="#500138", font=("Arial", 15))
        lbl_filtro_solar.place(x=12, y=45)
        btn_filtro_solar = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_filtro_solar, entry_filtro_solar, 10, 75, "Sim", "Não"),
        )
        btn_filtro_solar.place(x=225, y=47)
        entry_filtro_solar = ctk.CTkEntry(self, width=300, placeholder_text="Qual? E com que frequência?") 
        
        lbl_cosmetico_corporal = ctk.CTkLabel(self, text="Utiliza algum cosmético corporal?", text_color="#500138", font=("Arial", 15))
        lbl_cosmetico_corporal.place(x=12, y=105)
        btn_cosmetico_corporal = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_cosmetico_corporal, entry_cosmetico_corporal, 10, 135, "Sim", "Não"),
        )
        btn_cosmetico_corporal.place(x=225, y=105) #195 165
        entry_cosmetico_corporal = ctk.CTkEntry(self, width=300, placeholder_text="Qual(is)?") 
       
        lbl_tratamento_corporal = ctk.CTkLabel(self, text="Já fez algum tratamento corporal?", text_color="#500138", font=("Arial", 15))
        lbl_tratamento_corporal.place(x=12, y=165)
        btn_tratamento_corporal = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_tratamento_corporal, entry_tratamento_corporal, 10, 195, "Sim", "Não"),
        )
        btn_tratamento_corporal.place(x=225, y=165) #195 165
        entry_tratamento_corporal = ctk.CTkEntry(self, width=300, placeholder_text="Qual(is)?") 

        #QUEIXAS
        lbl_queixas = ctk.CTkLabel(self, text="Queixas", text_color="#500138", font=("Arial", 25))
        lbl_queixas.place(x=402,y=10)

        lbl_principal_queixa = ctk.CTkLabel(self, text="Qual a sua principal queixa?", text_color="#500138", font=("Arial", 15))
        lbl_principal_queixa.place(x=402, y=45)
        entry_principal_queixa = ctk.CTkEntry(self, width=300, placeholder_text="") 
        entry_principal_queixa.place(x=400,y=75)
        
        lbl_tempo_acontecimento = ctk.CTkLabel(self, text="A quanto tempo isso acontece?", text_color="#500138", font=("Arial", 15))
        lbl_tempo_acontecimento.place(x=402, y=105)
        entry_tempo_acontecimento = ctk.CTkEntry(self, width=300, placeholder_text="") 
        entry_tempo_acontecimento.place(x=400, y=135)
       
        lbl_agrave_queixa = ctk.CTkLabel(self, text="Existe algo que agrave sua queixa?", text_color="#500138", font=("Arial", 15))
        lbl_agrave_queixa.place(x=402, y=165)
        entry_agrave_queixa = ctk.CTkEntry(self, width=300, placeholder_text="Se sim, o que?") 
        entry_agrave_queixa.place(x=400, y=195)

        lbl_historico_familiar_queixa = ctk.CTkLabel(self, text="Existe algum histórico familiar de sua queixa?", text_color="#500138", font=("Arial", 15))
        lbl_historico_familiar_queixa.place(x=402, y=225)
        btn_historico_familiar_queixa = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_historico_familiar_queixa, None, None, None, "Sim", "Não"),
        )
        btn_historico_familiar_queixa.place(x=700, y=227) #195 165

        lbl_tratou_anteriormente = ctk.CTkLabel(self, text="Você já tratou sua queixa anteriormente?", text_color="#500138", font=("Arial", 15))
        lbl_tratou_anteriormente.place(x=402, y=265)
        btn_tratou_anteriormente = ctk.CTkButton(
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
            command=lambda: self.sim_nao(btn_tratou_anteriormente, entry_tratou_anteriormente, 400, 295, "Sim", "Não"),
        )
        btn_tratou_anteriormente.place(x=700, y=267) #195 165
        entry_tratou_anteriormente = ctk.CTkEntry(self, width=350, placeholder_text="Por quanto tempo? Qual foi o tratamento? Funcionou?")

        # Botão "Próximo"
        btn_proximo = ctk.CTkButton(
            self,
            text="Próximo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#500138",
            hover_color="#ffffff",
            corner_radius=8,
            width=100,
            height=30,
            command=self.ir_para_avaliacao,
        )
        btn_proximo.place(x=980, y=500)

    def ir_para_avaliacao(self):
        if self.controller:
            self.controller.atualizar_frame(Avaliacao)


class Avaliacao(ctk.CTkFrame):
    def sim_nao(self, nome_botao, nome_entry, x, y, opcao1, opcao2, opcao3=None):
        if nome_botao.cget("text") == opcao1:
            nome_botao.configure(text=opcao2, fg_color="red", anchor="e")
            if nome_entry and x and y != None:
                nome_entry.place_forget()
        elif nome_botao.cget("text") == opcao2:
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
        elif nome_botao.cget("text") == "Nulo":
            nome_botao.configure(text=opcao1, fg_color="green", anchor="w")
            if nome_entry and x and y != None:
                nome_entry.place(x=x, y=y)
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        # Configuração do frame para Dados Pessoais
        self.configure(fg_color="#ff85da", width=1100, height=554)

        lbl_fototipo_pele = ctk.CTkLabel(self, text="Fototipo de Pele", text_color="#500138", font=("Arial", 15))
        lbl_fototipo_pele.place(x=12, y=10)
        self.fototipo_pele = ctk.StringVar(value="")  # Variável para armazenar a escolha
        tb_tipo1 = ctk.CTkRadioButton(
            self, text="I", variable=self.fototipo_pele, value="I", fg_color="#500138", hover_color="#500138")
        tb_tipo1.place(x=12, y=40)

        rb_tipo2 = ctk.CTkRadioButton(
            self, text="II", variable=self.fototipo_pele, value="II", fg_color="#500138", hover_color="#500138"  )
        rb_tipo2.place(x=72, y=40)

        rb_tipo3 = ctk.CTkRadioButton(
            self, text="III", variable=self.fototipo_pele, value="III", fg_color="#500138", hover_color="#500138")
        rb_tipo3.place(x=132, y=40)
        
        rb_tipo4 = ctk.CTkRadioButton(
            self, text="IV", variable=self.fototipo_pele, value="IV", fg_color="#500138", hover_color="#500138")
        rb_tipo4.place(x=192, y=40)
        
        rb_tipo5 = ctk.CTkRadioButton(
            self, text="V", variable=self.fototipo_pele, value="V", fg_color="#500138", hover_color="#500138")
        rb_tipo5.place(x=252, y=40)
        
        rb_tipo6 = ctk.CTkRadioButton(
            self, text="VI", variable=self.fototipo_pele, value="VI", fg_color="#500138", hover_color="#500138")
        rb_tipo6.place(x=312, y=40)


        # Botão "Finalizar"
        btn_finalizar = ctk.CTkButton(
            self,
            text="Finalizar",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#500138",
            hover_color="#ffffff",
            corner_radius=8,
            width=100,
            height=30,
            command=self.finalizar_cadastro,
        )
        btn_finalizar.place(x=980,y=500)
    def finalizar_cadastro(self):
        print("Cadastro finalizado!")
        # Aqui você pode adicionar a lógica para salvar os dados ou navegar para outra tela.