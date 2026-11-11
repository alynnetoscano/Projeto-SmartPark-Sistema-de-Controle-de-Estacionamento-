
# SMARTPARK - SISTEMA DE CONTROLE DE ESTACIONAMENTO

# IMPORTAÇÃO DOS ARQUIVOS :)
import movimentacao
import relatorios as rel

from financeiro import (
    calcular_cobranca,
    consultar_faturamento,
    formatar_reais,
    mostrar_comprovante,
    mostrar_tabela_precos
)

from config import (
    CAPACIDADE_MAXIMA,
    TARIFA_HORA,
    HORA_ABERTURA,
    HORA_FECHAMENTO,
    OCUPACAO_INICIAL,
    FATURAMENTO_INICIAL
)


# CORES DO SISTEMA
AMARELO = "\033[33m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
NORMAL = "\033[0m"


# APRESENTAÇÃO DO SMARTPARK
def boas_vindas():

    print(AMARELO + "\n========================================" + NORMAL)
    print("            SMARTPARK")
    print("     CONTROLE DE ESTACIONAMENTO")
    print(AMARELO + "========================================" + NORMAL)
    nome = input("\nOlá! Digite seu nome: ")
    print(AMARELO + "\n========================================" + NORMAL)
    print(f"Olá, {nome}! Seja bem-vindo(a) ao SmartPark!")
    print("Facilitando a sua rotina.")
    print(AMARELO + "========================================" + NORMAL)

    return nome


# MENU PRINCIPAL
def mostrar_menu(nome, ocupadas):

    disponiveis = CAPACIDADE_MAXIMA - ocupadas

    print(AMARELO + "\n========================================" + NORMAL)
    print("              SMARTPARK")
    print(AMARELO + "========================================" + NORMAL)
    print(f"Usuário: {nome}")
    print(VERMELHO + "\n       INFORMAÇÕES IMPORTANTES" + NORMAL)
    print(f"Horário: {HORA_ABERTURA:02d}h às {HORA_FECHAMENTO:02d}h")
    print(f"Vagas disponíveis: {disponiveis}")
    print(f"Tarifa por hora: {formatar_reais(TARIFA_HORA)}")
    print(AMARELO + "\n----------- MENU PRINCIPAL -----------" + NORMAL)
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("5 - Relatório de movimentações")
    print("6 - Consultar tabela de preços")
    print("0 - Encerrar sistema")

    print(AMARELO + "--------------------------------------" + NORMAL)


# EXECUÇÃO PRINCIPAL PROFESSOR
def executar():
    ocupadas = OCUPACAO_INICIAL
    entradas = 0
    saidas = 0
    faturamento = FATURAMENTO_INICIAL
    funcionando = True


    nome = boas_vindas()


    while funcionando:

        mostrar_menu(nome, ocupadas)

        try:
            opcao = int(input("\nEscolha uma opção de 0 a 6: "))

        except ValueError:
            print(VERMELHO + "\nERRO! Por favor cliete um número valido :)." + NORMAL)

        else:
            if 0 <= opcao <= 6:

                match opcao:

                    case 1:
                        if movimentacao.registrar_entrada(ocupadas):
                            ocupadas += 1
                            entradas += 1

                    # REGISTRAR SAÍDA
                    case 2:
                        horas = movimentacao.registrar_saida(ocupadas)

                        if horas > 0:
                            valor = calcular_cobranca(horas)

                            ocupadas -= 1
                            saidas += 1
                            faturamento += valor

                            mostrar_comprovante(horas, valor)

                    # CONSULTAR VAGAS
                    case 3:
                        rel.consultar_vagas(ocupadas)

                    # CONSULTAR FATURAMENTO
                    case 4:
                        consultar_faturamento(faturamento, saidas)

                    # RELATÓRIO DE MOVIMENTAÇÕES
                    case 5:
                        rel.relatorio_movimentacoes(
                            entradas,
                            saidas,
                            ocupadas,
                            faturamento
                        )

                    # TABELA DE PREÇOS
                    case 6:
                        mostrar_tabela_precos()

                    # ENCERRAR SISTEMA
                    case 0:
                        print(AMARELO + "\n========================================" + NORMAL)
                        print("             RESUMO FINAL")
                        print(AMARELO + "========================================" + NORMAL)
                        print(f"Total de entradas: {entradas}")
                        print(f"Total de saídas: {saidas}")
                        print(f"Veículos estacionados: {ocupadas}")
                        print(f"Faturamento total: {formatar_reais(faturamento)}")
                        print(VERDE + f"\nObrigado por utilizar o SmartPark, {nome}!" + NORMAL)
                        print("Sistema encerrado com sucesso.")
                        print(AMARELO + "========================================" + NORMAL)
                        funcionando = False

            else:
                print(VERMELHO + "\nOPÇÃO INVÁLIDA! ESCOLHA DE 0 A 6." + NORMAL)

        finally:
            print(AMARELO + "----------------------------------------" + NORMAL)


# INICIAR O PROGRAMA
if __name__ == "__main__":
    executar()
