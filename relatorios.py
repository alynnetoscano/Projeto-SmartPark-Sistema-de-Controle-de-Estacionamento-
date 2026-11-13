"""Relatorios de ocupaçao e movimentaçao."""

from config import CAPACIDADE_MAXIMA
from financeiro import formatar_reais


def consultar_vagas(ocupadas):
    disponiveis = CAPACIDADE_MAXIMA - ocupadas
    percentual = (ocupadas / CAPACIDADE_MAXIMA) * 100

    if ocupadas == 0:
        situacao = "Estacionamento vazio"
    elif ocupadas == CAPACIDADE_MAXIMA:
        situacao = "Estacionamento lotado"
    else:
        situacao = "Vagas disponiveis"

    print("\n========== CONTROLE DE VAGAS ==========")
    print(f"Capacidade total: {CAPACIDADE_MAXIMA}")
    print(f"Vagas ocupadas: {ocupadas}")
    print(f"Vagas disponiveis: {disponiveis}")
    print(f"Taxa de ocupção: {percentual:.0f}%")
    print(f"Situação: {situacao}")
    print("=======================================")

def relatorio_movimentacoes(entradas, saidas, ocupadas, faturamento):
    disponiveis = CAPACIDADE_MAXIMA - ocupadas

    print("\n========== RELATORIO SMARTPARK ==========")
    print(f"Total de entradas: {entradas}")
    print(f"Total de saídas: {saidas}")
    print(f"Veiculos estacionados: {ocupadas}")
    print(f"Vagas disponíveis: {disponiveis}")
    print(f"Faturamento: {formatar_reais(faturamento)}")
    print("=========================================")