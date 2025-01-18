import mysql.connector 

class Conexao:
    def __init__(self, host="127.0.0.1", database="patp_ads2", port=3309, user="root", password="1234567890"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def conectar(self,query):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port)
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            print(f"Resultado: {resultado}")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

if __name__ == "__main__":
    Conexao().conectar("SELECT * FROM empresas") 
