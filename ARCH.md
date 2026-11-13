# 🏅 Arquitetura Medalhão (Medallion Architecture)

O projeto adota a arquitetura Medalhão, amplamente utilizada em plataformas modernas de dados como Databricks, Azure Data Lake, Microsoft Fabric e Apache Spark.

Essa abordagem organiza os dados em camadas progressivas de qualidade e enriquecimento, garantindo rastreabilidade, governança e facilidade de manutenção.

```text
CSVs Kaggle
     │
     ▼
┌─────────┐
│ BRONZE  │
└─────────┘
     │
     ▼
┌─────────┐
│ SILVER  │
└─────────┘
     │
     ▼
┌─────────┐
│  GOLD   │
└─────────┘
     │
     ▼
Dashboard / App
```

---

## 🥉 Bronze (Camada Raw)

Responsável pelo armazenamento dos dados brutos exatamente como foram obtidos da fonte original.

### Características

- Dados extraídos diretamente dos datasets do Kaggle.
- Conversão para formato Parquet.
- Particionamento por ano.
- Nenhum tratamento de negócio aplicado.
- Camada imutável.
- Garantia de rastreabilidade completa.

### Objetivos

- Preservar os dados originais.
- Permitir reprocessamentos futuros.
- Garantir reprodutibilidade das análises.

---

## 🥈 Silver Transacional

Camada responsável pela padronização e qualidade dos dados.

### Transformações

- Padronização da nomenclatura para `snake_case`.
- Conversão dos tipos de dados.
- Ajuste de datas.
- Conversão de valores booleanos.
- Remoção de registros duplicados.
- Aplicação de validações básicas.

### Benefícios

- Dados consistentes.
- Estrutura padronizada.
- Redução de erros analíticos.

---

## 🥈 Silver Contexto (Regras de Negócio)

Nesta camada são aplicadas as regras necessárias para transformar os dados técnicos em dados de negócio.

### Regras Implementadas

#### Resultados

- Determinação automática do vencedor da partida.
- Identificação de empates.

#### Vantagem de Mandante

- Cálculo do impacto de jogar em casa.
- Identificação de jogos em campo neutro.

#### Normalização Histórica

- Tratamento de mudanças históricas de nomes de seleções.
- Consolidação de países com diferentes nomenclaturas ao longo do tempo.

#### Integrações

Junção dos datasets:

- Results
- Goalscorers
- Shootouts

#### Criação de Dimensões

- Dimensão Time
- Dimensão Torneio
- Dimensão Data

---

## 🥇 Gold (Camada Analítica)

Camada voltada para consumo analítico, dashboards e modelos preditivos.

### Métricas Geradas

- Vitórias por seleção.
- Aproveitamento histórico.
- Média de gols marcados.
- Média de gols sofridos.
- Desempenho por torneio.
- Evolução por período.

### Ranking Elo

Implementação do cálculo de Elo Rating para seleções.

Período analisado:

```text
1872 → 2025
```

### Feature Engineering

Criação de atributos para modelos preditivos da Copa do Mundo 2026.

Exemplos:

- Elo Rating.
- Forma recente.
- Aproveitamento histórico.
- Média de gols.
- Performance em mata-mata.

### Simulações

Execução de simulações probabilísticas utilizando:

- Monte Carlo
- 10.000 iterações

Objetivo:

- Estimar probabilidades de classificação.
- Projetar favoritos ao título.
- Identificar cenários alternativos.

---

# 📊 Dashboard e Aplicação

A camada final disponibiliza os dados para consumo pelos usuários.

## Streamlit

O projeto utiliza Streamlit para construção do dashboard interativo.

### Funcionalidades

#### Previsões

- Campeão da Copa do Mundo 2026.
- Melhor ataque.
- Melhor defesa.
- Probabilidade de classificação.

#### Visualizações

- Evolução histórica das seleções.
- Ranking Elo.
- Comparativos entre equipes.
- Mapas de calor.
- Simulações Monte Carlo.
- Indicadores estatísticos.

---

# 🎯 Benefícios da Arquitetura

A utilização da arquitetura medalhão proporciona:

- Maior governança dos dados.
- Facilidade para auditorias.
- Reprocessamento simplificado.
- Melhor qualidade analítica.
- Separação clara entre ingestão, transformação e consumo.
- Escalabilidade para futuras integrações e fontes de dados.
