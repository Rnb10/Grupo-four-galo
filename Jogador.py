import soccerdata as sd
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configurações
liga = "ENG-Premier League"
temporada = "2022-2023"  # Temporada específica
diretorio_dados = "./dados"

# Criar pasta para salvar dados se não existir
os.makedirs(diretorio_dados, exist_ok=True)

# Inicializando o scraper
fbref = sd.FBref(leagues=[liga], seasons=[temporada])

try:
    print(f"Processando a liga: {liga}")
    # Lendo as estatísticas da temporada (tipo padrão)
    dados = fbref.read_team_season_stats(stat_type="standard")

    # Resolver MultiIndex para colunas simples
    if isinstance(dados.columns, pd.MultiIndex):
        dados.columns = dados.columns.to_flat_index()
        dados.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in dados.columns]

    # Usar nomes dos times como índice
    dados.index = dados.index.get_level_values("team")

    # Selecionar as colunas relevantes
    colunas_selecionadas = [
        "Performance_Gls",      # Gols
        "Performance_Ast",      # Assistências
        "Performance_G+A",      # Gols + Assistências
        "Performance_CrdY",     # Cartões Amarelos
        "Performance_CrdR",     # Cartões Vermelhos
        "Expected_xG",          # Gols esperados
        "Expected_xAG",         # Assistências esperadas
        "Progression_PrgC",     # Passes progressivos recebidos
        "Progression_PrgP"      # Passes progressivos realizados
    ]
    dados_filtrados = dados[colunas_selecionadas].copy()

    # Salvar dados em CSV
    caminho_csv = os.path.join(diretorio_dados, f"{liga}_dados_{temporada}.csv")
    dados_filtrados.to_csv(caminho_csv, index=True)
    print(f"Dados salvos em: {caminho_csv}")

    # Gráfico de Barras - Gols e Assistências por Time
    plt.figure(figsize=(12, 6))
    dados_filtrados[["Performance_Gls", "Performance_Ast"]].plot(kind="bar", stacked=True, figsize=(12, 6), alpha=0.8)
    plt.title(f"Gols e Assistências por Time - {temporada}")
    plt.ylabel("Quantidade")
    plt.xlabel("Times")
    plt.xticks(rotation=45)
    plt.tight_layout()
    caminho_barras_empilhadas = os.path.join(diretorio_dados, f"{liga}_gols_assistencias_empilhadas_{temporada}.png")
    plt.savefig(caminho_barras_empilhadas)
    print(f"Gráfico de barras empilhadas salvo em: {caminho_barras_empilhadas}")
    plt.close()

    # Gráfico de Barras Horizontais - Cartões Amarelos e Vermelhos
    plt.figure(figsize=(12, 6))
    dados_filtrados[["Performance_CrdY", "Performance_CrdR"]].plot(kind="barh", stacked=False, figsize=(12, 6), alpha=0.8, color=["yellow", "red"])
    plt.title(f"Cartões Amarelos e Vermelhos por Time - {temporada}")
    plt.xlabel("Quantidade")
    plt.ylabel("Times")
    plt.tight_layout()
    caminho_barras_horizontais = os.path.join(diretorio_dados, f"{liga}_cartoes_{temporada}.png")
    plt.savefig(caminho_barras_horizontais)
    print(f"Gráfico de barras horizontais salvo em: {caminho_barras_horizontais}")
    plt.close()

    # Gráfico de Linhas - Progressão por Time
    plt.figure(figsize=(12, 6))
    plt.plot(dados_filtrados.index, dados_filtrados["Progression_PrgC"], label="Passes Progressivos Recebidos", marker='o')
    plt.plot(dados_filtrados.index, dados_filtrados["Progression_PrgP"], label="Passes Progressivos Realizados", marker='x')
    plt.title(f"Progressão de Passes por Time - {temporada}")
    plt.ylabel("Quantidade")
    plt.xlabel("Times")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    caminho_linhas_progressao = os.path.join(diretorio_dados, f"{liga}_progressao_passes_{temporada}.png")
    plt.savefig(caminho_linhas_progressao)
    print(f"Gráfico de linhas salvo em: {caminho_linhas_progressao}")
    plt.close()

        # Gráfico de Pizza - Proporção de Gols e Assistências
    plt.figure(figsize=(8, 8))
    total_gols = dados_filtrados["Performance_Gls"].sum()
    total_assistencias = dados_filtrados["Performance_Ast"].sum()
    labels = ["Gols", "Assistências"]
    sizes = [total_gols, total_assistencias]
    colors = ["#ff9999", "#66b3ff"]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(f"Proporção de Gols e Assistências - {temporada}")
    caminho_pizza = os.path.join(diretorio_dados, f"{liga}_gols_assistencias_pizza_{temporada}.png")
    plt.savefig(caminho_pizza)
    print(f"Gráfico de pizza salvo em: {caminho_pizza}")
    plt.close()

    # Gráfico de Dispersão - Comparação entre xG e Gols
    plt.figure(figsize=(12, 6))
    plt.scatter(dados_filtrados["Expected_xG"], dados_filtrados["Performance_Gls"], color="blue", alpha=0.7)
    plt.title(f"Comparação entre xG e Gols por Time - {temporada}")
    plt.xlabel("xG (Gols Esperados)")
    plt.ylabel("Gols")
    for i, team in enumerate(dados_filtrados.index):
        plt.text(dados_filtrados["Expected_xG"][i], dados_filtrados["Performance_Gls"][i], team, fontsize=9)
    caminho_dispersao = os.path.join(diretorio_dados, f"{liga}_xG_gols_dispersao_{temporada}.png")
    plt.savefig(caminho_dispersao)
    print(f"Gráfico de dispersão salvo em: {caminho_dispersao}")
    plt.close()

    # Gráfico de Barras Empilhadas - xG e xAG por Time
    plt.figure(figsize=(12, 6))
    dados_filtrados[["Expected_xG", "Expected_xAG"]].plot(kind="bar", stacked=True, figsize=(12, 6), alpha=0.8, color=["#72A0C1", "#F4A460"])
    plt.title(f"xG e xAG por Time - {temporada}")
    plt.ylabel("Quantidade")
    plt.xlabel("Times")
    plt.xticks(rotation=45)
    plt.tight_layout()
    caminho_xg_xag_barras = os.path.join(diretorio_dados, f"{liga}_xg_xag_empilhadas_{temporada}.png")
    plt.savefig(caminho_xg_xag_barras)
    print(f"Gráfico de barras empilhadas para xG e xAG salvo em: {caminho_xg_xag_barras}")
    plt.close()

    # Gráfico de Linhas - xG, xAG e Gols por Time
    plt.figure(figsize=(12, 6))
    plt.plot(dados_filtrados.index, dados_filtrados["Expected_xG"], label="xG (Gols Esperados)", marker='o', color="blue")
    plt.plot(dados_filtrados.index, dados_filtrados["Expected_xAG"], label="xAG (Assistências Esperadas)", marker='x', color="orange")
    plt.plot(dados_filtrados.index, dados_filtrados["Performance_Gls"], label="Gols Marcados", marker='s', color="green")
    plt.title(f"xG, xAG e Gols por Time - {temporada}")
    plt.ylabel("Quantidade")
    plt.xlabel("Times")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    caminho_linhas_xg_xag = os.path.join(diretorio_dados, f"{liga}_linhas_xg_xag_gols_{temporada}.png")
    plt.savefig(caminho_linhas_xg_xag)
    print(f"Gráfico de linhas para xG, xAG e Gols salvo em: {caminho_linhas_xg_xag}")
    plt.close()

    # Gráfico de Tabela - Resumo Estatístico
    plt.figure(figsize=(10, 4))
    tabela = dados_filtrados[["Performance_Gls", "Performance_Ast", "Expected_xG", "Expected_xAG"]].reset_index()
    tabela.columns = ["Time", "Gols", "Assistências", "xG", "xAG"]
    cell_text = tabela.values
    plt.table(cellText=cell_text, colLabels=tabela.columns, loc='center', cellLoc='center', colLoc='center')
    plt.axis('off')
    plt.title(f"Resumo Estatístico - {temporada}", y=1.05)
    caminho_tabela = os.path.join(diretorio_dados, f"{liga}_tabela_estatisticas_{temporada}.png")
    plt.savefig(caminho_tabela)
    print(f"Gráfico de tabela salvo em: {caminho_tabela}")
    plt.close()

    # Gráfico de Linhas - Cartões ao Longo da Temporada
    plt.figure(figsize=(12, 6))
    plt.plot(dados_filtrados.index, dados_filtrados["Performance_CrdY"], label="Cartões Amarelos", marker='o', color="yellow")
    plt.plot(dados_filtrados.index, dados_filtrados["Performance_CrdR"], label="Cartões Vermelhos", marker='x', color="red")
    plt.title(f"Cartões por Time - {temporada}")
    plt.ylabel("Quantidade")
    plt.xlabel("Times")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    caminho_linhas_cartoes = os.path.join(diretorio_dados, f"{liga}_linhas_cartoes_{temporada}.png")
    plt.savefig(caminho_linhas_cartoes)
    print(f"Gráfico de linhas para Cartões salvo em: {caminho_linhas_cartoes}")
    plt.close()

except KeyError as e:
    print(f"Erro ao processar a liga {liga}: {e}")
except Exception as e:
    print(f"Erro inesperado ao processar a liga {liga}: {e}")
