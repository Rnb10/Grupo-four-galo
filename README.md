# Projeto: Estatísticas de Ligas de Futebol

Este projeto realiza a análise de estatísticas de ligas de futebol utilizando a biblioteca `soccerdata` em Python. Ele gera gráficos e arquivos CSV com informações detalhadas de desempenho por time.

## Ligas Disponíveis

As seguintes ligas podem ser pesquisadas:

- `ENG-Premier League`
- `ESP-La Liga`
- `FRA-Ligue 1`
- `GER-Bundesliga`
- `ITA-Serie A`

## Anos Disponíveis

Os seguintes anos estão disponíveis para análise:

- `2022-2023`
- `2021-2022`
- `2020-2021`

Para alterar o ano ou a liga, edite as variáveis `ligas` e `temporadas` no código.

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.9 ou superior
- pip
- Virtualenv

## Passo a Passo para Configuração

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-repositorio/aqui.git
```
```bash
cd nome-do-repositorio
```
Crie o ambiente virtual:
 ```bash
python -m venv venv
 ```
Ative o ambiente virtual:

Windows:
 ```bash
venv\Scripts\activate
 ```
Linux/Mac:
 ```bash
source venv/bin/activate
 ```
Instale as dependências:
 ```bash
pip install -r requirements.txt
 ```
Executando o Projeto

Edite o arquivo Jogador.py para ajustar a liga e a temporada conforme necessário.
Execute o script principal:
 ```bash
python Jogador.py
 ```
Resultados
Arquivo CSV gerado: ./dados/[NOME_LIGA]_dados_[ANO].csv
Gráficos gerados:
Gráfico de barras: ./dados/[NOME_LIGA]_gols_barras_[ANO].png
Gráfico de pizza: ./dados/[NOME_LIGA]_assistencias_pizza_[ANO].png
Outros gráficos (variação conforme script): ./dados/
Observação
Caso ocorra algum erro relacionado à biblioteca soccerdata, consulte a documentação oficial para possíveis soluções.

