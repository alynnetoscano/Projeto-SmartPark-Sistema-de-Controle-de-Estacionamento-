"""CobranÃ§as, comprovantes e faturamento."""

from config import TARIFA_HORA, PERMANENCIA_MINIMA, HORA_ABERTURA, HORA_FECHAMENTO


def formatar_reais(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def calcular_cobranca(horas):
    if horas < PERMANENCIA_MINIMA:
        horas = PERMANENCIA_MINIMA
    return float(horas) * TARIFA_HORA


def mostrar_comprovante(horas, valor):
    print("\n========== COMPROVANTE ==========")
    print(f"Tempo de permanencia: {horas} hora(s)")
    print(f"Tarifa por hora: {formatar_reais(TARIFA_HORA)}")
    print(f"Valor a pagar: {formatar_reais(valor)}")
    print("Saida registrada com sucesso!")
    print("=================================")


def consultar_faturamento(faturamento, saidas):
    if saidas == 0:
        media = 0.0
    else:
        media = faturamento / saidas

    print("\n========== FATURAMENTO ==========")
    print(f"Total arrecadado: {formatar_reais(faturamento)}")
    print(f"Saidas registradas: {saidas}")
    print(f"Media por saida: {formatar_reais(media)}")
    print("=================================")


def mostrar_tabela_precos():
    print("\n========== TABELA DE PREÇOS ==========")
    print(f"Funcionamento: {HORA_ABERTURA:02d}h Ã s {HORA_FECHAMENTO:02d}h")
    print(f"Tarifa por hora: {formatar_reais(TARIFA_HORA)}")
    print(f"Permanencia minima: {PERMANENCIA_MINIMA} hora(s)")

    for horas in range(1, 6):
        valor = calcular_cobranca(horas)
        print(str(horas) + " hora(s): " + formatar_reais(valor))

    print("======================================")