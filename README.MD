## Arquitetura Medalhão

### Bronze (Camada Raw - Marrom)
- Dados exatamente como extraídos dos CSVs do Kaggle
- Formato Parquet particionado por ano
- Imutável: garante reprodutibilidade e rastreabilidade

### Silver Transacional
- Padronização de nomenclatura (snake_case)
- Conversão de tipos (date, boolean)
- Remoção de duplicatas e validações básicas

### Silver Contexto (Regras de Negócio)
- Aplicação de regras: cálculo de vencedor, vantagem de jogar em casa
- Junção entre tabelas (results + goalscorers + shootouts)
- Tratamento de mudanças históricas de nomes de seleções
- Criação de dimensões (time, torneio, data)

### Gold (Métricas e Estatísticas)
- Agregações para análise de desempenho
- Cálculo de ranking Elo rating (1872-2025)
- Features para modelo preditivo da Copa 2026
- Simulações Monte Carlo (10.000 iterações)

### BI/APP
- Dashboard interativo com Streamlit
- Previsões: campeão, melhor ataque, melhor defesa
- Visualizações: evolução histórica, mapa de calor, simulações 