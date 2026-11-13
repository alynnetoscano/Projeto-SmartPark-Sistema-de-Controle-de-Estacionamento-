<<<<<<< HEAD
# Projeto-SmartPark-Sistema-de-Controle-de-Estacionamento-
# SmartPark — Sistema de Controle de Estacionamento

Projeto Fase 01 da disciplina **Programação Estruturada em Python**.
Sistema de terminal que controla entrada e saída de veículos, ocupação das vagas, cobrança e faturamento.

## Integrantes
- Alynne Toscano Vasconcelos
- Gustavo Oliveira Calvalcante
- Matheus Alves Azevedo Calvalcanti Machado

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
git clone https://github.com/alynnetoscano/Projeto-SmartPark-Sistema-de-Controle-de-Estacionamento-.git
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
=======
# SmartPark — Sistema de Controle de Estacionamento

Projeto da **Fase 01** da disciplina de Programação Estruturada em Python.

## Objetivo

Controlar entradas e saídas de veículos, a ocupação das vagas e o faturamento de um estacionamento por meio de um programa de terminal.

## Funcionalidades

- Registrar entrada de veículos, respeitando o limite de 20 vagas.
- Registrar saída com permanência inteira e positiva.
- Calcular cobrança de R$ 5,00 por hora, com permanência mínima de uma hora.
- Consultar vagas ocupadas, disponíveis e percentual de ocupação.
- Consultar faturamento acumulado e média por saída.
- Exibir relatório de movimentações.
- Mostrar tabela de preços de 1 a 5 horas.
- Encerrar com resumo de entradas, saídas e faturamento.

## Requisitos

- Python **3.10 ou superior**.
- Nenhuma biblioteca externa é necessária.

## Como executar

1. Clique em **Code > Download ZIP** no GitHub.
2. Extraia o arquivo ZIP.
3. Abra a pasta extraída no PyCharm.
4. Configure um interpretador Python 3.10 ou superior.
5. Abra `main.py` e escolha **Run 'main'**.

Ou, com o terminal aberto na pasta do projeto:

```bash
python main.py
```

Em alguns computadores Windows, também funciona `py main.py`.

## Organização dos arquivos

- `main.py` — menu principal e variáveis de controle do nosso projeto :).
- `movimentacao.py` — regras de entrada e saída.
- `financeiro.py` — cálculos e consultas de faturamento.
- `relatorios.py` — relatórios de vagas e movimentações.
- `config.py` — constantes e configurações.
- `README.md` — documentação do projeto.
- `.gitignore` — arquivos que não precisam ser publicados.

## Configuração e observações

- Capacidade: 20 vagas.
- Tarifa: R$ 5,00 por hora.
- Horário informado: 06h às 22h.
- A aplicação não faz controle pelo relógio do computador.
- Não registra placas nem horários individuais.
- Os dados ficam na memória e são reiniciados quando o programa é aberto novamente.

>>>>>>> 8a0a5ec (subindo arquivos)
