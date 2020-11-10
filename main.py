from idade import Idade  # importando a classe idade
from datetime import date  # importando a biblioteca de data

print("Programa para calcular a idade")  # Nome do Programa
print("BEM VINDO!!!\nVAMOS  DESCOBRIR A SUA IDADE")  # boas vindas
data_atual = date.today()
data_em_string = data_atual.strftime("%d/%m/%Y")
print("Hoje é dia {}".format(data_em_string))


def inicio():  # definindo a função
    ano = date.today()  # passando o dia, mes e ano para a váriável ano
    ano_texo = ano.strftime('%Y')  # convertendo meu ano em string e pegando somente o ano e levando para uma nova váriável,
    ano_int = int(ano_texo)  # em sring e repetindo a operação para mes e ano.
    mes = date.today()
    mes_texto = mes.strftime('%m')
    mes_int = int(mes_texto)
    dia = date.today()
    dia_texto = dia.strftime('%d')
    dia_int = int(dia_texto)
    anoNasc = 0  # iniciando minhas variáveis que receberão os valores do usuário em 0
    mesNasc = 0
    diaNasc = 0

    '''
    Para ser bissexto, o ano deve ser:
    Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
    Não pode ser divisível por 100.
    Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
    Pode ser que seja divisível por 400.
    Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
    com essas informações, montamos a lógica contra essa condição
    '''

    def bissexto():  # função para verficar se ano é bissexto
        if anoNasc % 100 == 0:  # resto da divisão igual a zero verificamos uma segunda condição por 400
            if anoNasc % 400 != 0:  # resto da divisão por 400 se for diferente de zero, não é bissexto
                print("Esse ano nao e bissexto, portanto nao possui 29 de fevereiro.\nMês incorreto, Tente novamente!!!")
                inicio()  # reiniciamos o programa
        elif anoNasc % 100 != 0:  # se resto da divisão for diferente de zero testamos mais uma condição
            if anoNasc % 4 != 0:  # se a divisão não é exata e o resto é diferente de zero, não é bissexto
                print("Esse ano nao e bissexto, portanto nao possui 29 de fevereiro.\nMês incorreto, Tente novamente!!!")
                inicio()  # reiniciamos o programa
        print("Ano de nascimento é bissexto.")  # atendeu todas as exigencias da função. É Bissexto.

    try:  # utilizamos o try para tratar teclas que não sejam numéricas
        anoNasc = int(input("Qual o Ano do seu nascimento:\n-->"))
        if anoNasc > ano_int or anoNasc < 1900:  # condicionando o ano recebido
            print("Ano incompátivel com ano atual, você não pode ser do futuro!\nSomente acima de 1900 e menor ou igual ao ano atual.\nDigite novamente!")
            inicio()  # reiniciando o programa
        mesNasc = int(input("Qual o mes do nascimento:\n-->"))  # recebendo os paramentros as datas do usuário e
        if anoNasc == ano_int and mesNasc > mes_int:
            print("Mês incompátivel com ano atual, você não pode ser do futuro. Digite novamente!!!")
            inicio()
        if mesNasc > 12 or mesNasc < 1:
            print("Mês inválido. Digite novamente!!!")  # validando as datas conforme o mes
            inicio()  # reiniciando o programa
        diaNasc = int(input("Qual o dia do seu nascimento:\n-->"))  # setando nas minhas variáveis
        if anoNasc == ano_int and mesNasc >= mes_int and diaNasc > dia_int:
            print("Dia incompátivel com ano e mês atual, você não pode ser do futuro. Digite novamente!!!")
            inicio()
        if diaNasc > 32 or diaNasc < 1:
            print("Dia inválido. Digite novamente!!!")  # validando as datas conforme o mes
            inicio()  # reiniciando o programa
        if mesNasc == 1 or mesNasc == 3 or mesNasc == 5 or mesNasc == 7 or mesNasc == 8 or mesNasc == 10 or mesNasc == 12:
            if diaNasc > 31:
                print("Esses mes possui somente 31 dias.\nDigite Novamente!!!")
                inicio()  # reiniciando o programa
        elif mesNasc == 4 or mesNasc == 6 or mesNasc == 9 or mesNasc == 11:
            if diaNasc > 30:
                print("Esse mes possui somente 30 dias.\nDigite Novamente!!!")
                inicio()  # reiniciando o programa
        if mesNasc == 2:  # Caso seja fevereiro temos apenas 28 dias (A implementar um calculo para ano bissexto)
            if diaNasc > 29:
                print("Dia inexitente para o mês de Fevereiro. Tente novamente!!!")
                inicio()  # reiniciando o programa
            elif diaNasc == 29:
                print("Fevereiro tem no maximo 29 dias, se for bissexto.\nVamos Verificar!!!")
                bissexto()  # se fevereiro for igual a dia 29 verificamos se é bissexto
    except ValueError:  # excessão do try, valor recebido errado, que não seja número
        print("Opção inválida, Não utilize letras, ponto, virgula ou deixe vazio!\nA entrada deve ser um número inteiro , conforme a pergunta!\nPor Favor, tente novamente!!!")
        inicio()  # reiniciando o programa

    minhaIdade = Idade(anoNasc, mesNasc, diaNasc)  # instaciando a classe
    idadeanos = minhaIdade.calcularAnos()  # recebendo o calculo de anos da classe idade
    idademeses = minhaIdade.calcularMeses()  # recebendo o calculo dos meses da classe idade
    idadedias = minhaIdade.calcularDias()  # recebendo o calculo dos dias da classe idade
    print("Você tem {} Anos. ".format(idadeanos))
    print("A sua idade em meses é aproximadamente {} Meses. ".format(idademeses))  # printando os resultados
    print("A sua idade em dias é aproximadamente {} dias.  ".format(idadedias))
    exit()  # encerrando o programa


inicio()  # iniciando o programa