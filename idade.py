from datetime import date

class Idade: # definindo a classe

    def __init__(self, anoNasc, mesNasc, diaNasc):  # inicializando
        self.anonasc = anoNasc  # passando o raio pra váriavel
        self.mesnasc = mesNasc  # iniciando minha area sem valor
        self.dianasc = diaNasc  # iniciando meu perimetro sem valor
        self.dia = date.today() # passando a data atual do sistema para a variável
        self.totalAnos = 0  #iniciando minhas variáveis em 0 para retorna a classe main com valores
        self.totalMeses = 0
        self.totalDias = 0



    def calcularAnos(self): # função para calcular os anos
        self.nova_data_texo = self.dia.strftime('%d/%m/%Y')  # transformando a data em string com a função datetime
        self.novo_dia_int = int(self.nova_data_texo[0] + self.nova_data_texo[1])
        self.novo_mes_int = int(self.nova_data_texo[3] + self.nova_data_texo[4])
        self.novo_ano_int = int(self.nova_data_texo[6] + self.nova_data_texo[7] + self.nova_data_texo[8] + self.nova_data_texo[9])
        #chamando a data em string conforme a posição desejada
        if self.novo_dia_int >= self.dianasc or self.novo_mes_int >= self.mesnasc:
            self.totalAnos = self.novo_ano_int - self.anonasc    # atendendo as condições, feliz aniversário
            return self.totalAnos
        else:
            self.totalAnos = self.novo_ano_int - self.anonasc - 1  # se não completou aniversário no ano vigente
            return self.totalAnos                                 #subtraimos 1 ano


    def calcularMeses(self): # função para calcular os meses
        self.totalMeses = self.totalAnos * 12 + self.novo_mes_int
        return self.totalMeses

    def calcularDias(self): #função para calcular os dias
        self.totalDias = self.totalAnos * 365 + self.novo_mes_int * 30
        return self.totalDias   #calculando a idade em dias aproximado








