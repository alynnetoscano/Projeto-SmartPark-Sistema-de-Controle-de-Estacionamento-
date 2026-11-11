# Projeto-SmartPark-Sistema-de-Controle-de-Estacionamento-
# SmartPark — Sistema de Controle de Estacionamento

Projeto Fase 01 da disciplina **Programação Estruturada em Python**.
Sistema de terminal que controla entrada e saída de veículos, ocupação das vagas, cobrança e faturamento.

## Integrantes
- Alynne 
- Gustavo 
- Matheus 

## Funcionalidades
- Registrar entrada de veículo (bloqueia quando lotado)
- Registrar saída com cálculo de cobrança e comprovante
- Consultar vagas disponíveis e taxa de ocupação
- Consultar faturamento, nº de saídas e valor médio
- Relatório de movimentações
- Tabela de preços (simulação de 1 a 5 horas)
- Encerramento com resumo final

## Requisitos
- Python 3.10 ou superior (usa `match...case`)
- Nenhuma biblioteca externa

## Como executar
```bash
git clone https://github.com/SEU_USUARIO/smartpark-python.git
cd smartpark-python
python main.py
```

## Estrutura
| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Menu principal e controle da execução (guarda contadores e faturamento) |
| `movimentacao.py` | Regras de entrada e saída de veículos |
| `financeiro.py` | Cálculos de cobrança e faturamento |
| `relatorios.py` | Exibição de relatórios |
| `config.py` | Constantes do sistema |

## Configurações
20 vagas · R$ 5,00/hora · 06h às 22h · permanência mínima de 1 hora.
