"""Regras para entrada a saída dos veiculos."""

from config import CAPACIDADE_MAXIMA


def registrar_entrada(ocupadas):
    """Retorna True quando a entrada pode ser realizada."""
    if not (ocupadas >= 0 and ocupadas < CAPACIDADE_MAXIMA):
        print("\nEntrada recusada: estacionamento lotado ou ocupação invalida.")
        return False

    disponiveis = CAPACIDADE_MAXIMA - (ocupadas + 1)
    print("\nEntrada registrada com sucesso!")
    print(f"Vagas disponiveis: {disponiveis}")
    return True


def registrar_saida(ocupadas):
    """Solicita horas validas e devolve 0 se o estacionamento estiver vazio."""
    if ocupadas <= 0 or ocupadas > CAPACIDADE_MAXIMA:
        print("\nSaida recusada: não há veiculos para retirar.")
        return 0

    while True:
        try:
            horas = int(input("\nDigite as horas de permanencia: "))
        except ValueError:
            print("Valor invalido! Digite um número inteiro, como 2.")
        else:
            if horas <= 0:
                print("Tempo invalido! Informe pelo menos 1 hora.")
            else:
                return horas