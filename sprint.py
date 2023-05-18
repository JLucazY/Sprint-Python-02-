#módulos usados
import re
import unicodedata
import random
#sorteio do horário da visita
hora_random = random.randint(1,3)
match hora_random:
    case 1:
        hora = "9:30"
    case 2:
        hora = "10:30"
    case 3:
        hora = "11:30"
#validação no nome do usuário
while True:
    nome = input("Digite seu nome: ")
    nome_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', nome) if unicodedata.category(c) != 'Mn')
    if re.match("^[a-zA-Z ]+$", nome_sem_acentos):
        break
    else:
        print("Por favor, digite um nome válido! (sem números)")

#laço do menu       
laco = True
while laco == True:
    print(f"Bem vindo {nome}!")
    while True:
        print("""
                ------------------------
                         MENU
                ------------------------
                    1 - Orçamento
                    2 - Sobre nós
                    3 - Sair
                """)
        #valida a escolha e move para a página desejada
        try: 
            menu = int(input())
            if not type(menu) is int:
                raise ValueError
            elif menu <= 0 or menu >= 4:
                print("Digite um número correspondente!")
                continue
            else:
                break
                
        except ValueError:
            print("Digite apenas números!")
            continue
            
    
    #apresenta a lista de serviços da empresa
    if menu == 1:
        print("""Lista de serviços:
                    1 - Previsão de economia
                    2 - inspeção técnica no local
                    3 - Instalação de painéis solares
                    4 - Voltar
                    (Digite qualquer outro numero para encerrar)""")
        #usuário escolhe qual serviço se apropria a necessidade dele
        tipo_servico = int(input())
        # match tipo_servico:
        if tipo_servico == 1:
                while True:
                    try:
                        conta_luz = float(input("Digite o preço de sua conta de luz: R$"))
                        if not type(conta_luz) is float:
                            raise ValueError
                        conta_desconto = conta_luz * 0.8
                        print(f"{nome}, baseado em cálculos aritméticos, a conta de luz que o senhor(a) pagará após a eficiência energética é de {conta_desconto:.2f}!")
                        break
                    except ValueError:
                        print("Digite apenas números!")     
                        continue
        elif tipo_servico == 2:
                while True:
                    print("digite o dia para a realização da inspeção")
                    try:
                        dia = int(input())
                        if not type(dia) is int:
                            raise ValueError
                        elif dia <= 31 and dia >= 1:
                            print(f"Agendado senhor(a) {nome}, o dia para a realização da inspeção será {dia} ás {hora}!")
                            break
                        else:
                            print("Dia inválido! Digite um dia valido")
                        continue
                    except ValueError:
                        print("Digite apenas números!")
                        continue
        elif tipo_servico == 3:
                while True:
                    try:   
                        print("Nos informe a quantidade de espaço, em m²,disponível para a instalação")
                        m = float(input())
                        if not type(m) is float:
                            raise ValueError
                        preco_painel_solar = m * 100
                        print(f"Senhor(a) {nome}, o orçamento de instalação será de: R${preco_painel_solar:.2f}")
                        break
                    except ValueError:
                        print("Digite apenas números")
                        continue
        elif tipo_servico == 4:
            continue
        
        else: 
            break
                
    if menu == 2:
        print("""
                Buscamos oferecer soluções customizadas que atendam suas demandas. 
                Trazendo-lhe alternativas que visam uma maior economia, eficiência e segurança energética, 
                estimulando a sustentabilidade e a competitividade para que você tenha um destaque ainda maior no mercado.
                
                Soluções usadas por nós:
                    1 - Uso de fontes de energia renováveis
                    2 - Monitoramento e gerenciamento de energia
                    3 - Melhorias na eficiência dos equipamentos
                """)
        print("(1) Voltar  (2) Sair")
        decisao = int(input())
        match decisao:
            case 1: 
                    menu = 1
            case 2:
                    laco = False
        
    else:
        laco = False    

print(f"Obrigado por confiar em nós, volte sempre {nome}")