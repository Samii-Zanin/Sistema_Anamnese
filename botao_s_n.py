import customtkinter as ctk
class Botao():
    def __init__(self, root):
        def toggle_switch(nome_botao):
            if nome_botao.cget("text") == "Sim":
                nome_botao.configure(text="Não", fg_color="red", anchor="e")
            elif nome_botao.cget("text") == "Não":
                nome_botao.configure(text="Sim", fg_color="green", anchor="w")
            elif nome_botao.cget("text") == "Nulo":
                nome_botao.configure(text="Sim", fg_color="green", anchor="w")
        self.root = root
        self.root.title("Interruptor Sim/Não")
        self.root.geometry("400x200")

        frame = ctk.CTkFrame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        switch_button = ctk.CTkButton(
            frame,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",  # Cor inicial
            text_color="black",
            hover_color="white",
            corner_radius=8,  # Arredondamento das bordas
            width=150,  # Largura do botão
            height=40,  # Altura do botão
            anchor="center",  # Alinhamento do texto
            command=lambda: toggle_switch(switch_button),
        )
        switch_button.pack(pady=10)

        # Botão 2 estilizado
        botao2 = ctk.CTkButton(
            frame,
            text="Nulo",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="gray",  # Cor inicial
            text_color="black",
            hover_color="white",
            corner_radius=80,  # Arredondamento das bordas
            width=150,  # Largura do botão
            height=40,  # Altura do botão
            anchor="center",  # Alinhamento do texto
            command=lambda: toggle_switch(botao2),
        )
        botao2.pack(pady=10)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = Botao()
    app.run()
