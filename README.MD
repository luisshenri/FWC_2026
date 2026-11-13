# ⚽ FWC_2026 - FIFA World Cup 2026 Data Engineering Project

## 📖 Sobre o Projeto

O **FWC_2026** é um projeto de Engenharia de Dados desenvolvido com foco na **Copa do Mundo FIFA 2026**, tendo como objetivo coletar, processar, armazenar e analisar dados relacionados ao maior evento de futebol do mundo.

A proposta do projeto é aplicar conceitos modernos de Engenharia de Dados em um cenário real, envolvendo coleta de informações esportivas, processamento de dados, modelagem analítica, geração de indicadores e construção de bases preparadas para análises e visualizações.

Além do aspecto técnico, o projeto foi desenvolvido como parte da evolução profissional e prática em tecnologias voltadas para Data Engineering, Data Analytics e Business Intelligence.

> ⚠️ Projeto desenvolvido para fins de estudo, aprendizado, portfólio e aperfeiçoamento técnico em Engenharia de Dados.

---

# 🎯 Objetivos do Projeto

- Aplicar conceitos de Engenharia de Dados em um caso de uso real.
- Desenvolver pipelines de ingestão e transformação de dados.
- Estruturar datasets para análises esportivas.
- Implementar processos ETL e ELT.
- Consolidar informações relacionadas à Copa do Mundo FIFA 2026.
- Gerar indicadores e insights analíticos.
- Desenvolver experiência prática em arquitetura de dados.

---

# 🌳 Estratégia de Branches

O projeto utiliza uma estrutura de versionamento baseada em branches para separar o ambiente estável do ambiente de desenvolvimento.

| Branch | Objetivo |
|----------|----------|
| `main` | Versão principal e estável do projeto |
| `dev` | Desenvolvimento e evolução contínua das funcionalidades |

## 🔹 Branch Main

A branch **main** representa a versão principal e consolidada do projeto.

Características:

- Código validado.
- Funcionalidades estáveis.
- Estrutura consolidada.
- Base para demonstrações.
- Referência para futuras releases.

## 🔹 Branch Dev

A branch **dev** é utilizada para desenvolvimento ativo do projeto.

Características:

- Implementação de novos recursos.
- Testes de pipelines.
- Evolução da arquitetura de dados.
- Desenvolvimento de análises adicionais.
- Experimentação de melhorias antes da publicação.

### Fluxo de Trabalho

```text
dev
 ↓
Validação
 ↓
main
```

Toda funcionalidade nova deve ser desenvolvida inicialmente na branch `dev` antes de ser integrada à branch principal.

---

# 🚀 Funcionalidades

## 📥 Coleta de Dados

- Extração de dados esportivos.
- Integração com fontes públicas.
- Coleta de estatísticas de partidas.
- Armazenamento de informações históricas.

## ⚙️ Processamento de Dados

- Limpeza de dados.
- Tratamento de inconsistências.
- Padronização de registros.
- Transformação e enriquecimento de informações.
- Validação de qualidade dos dados.

## 🗄️ Armazenamento

- Organização de datasets.
- Estruturação para análises futuras.
- Separação por camadas de processamento.
- Persistência de dados tratados.

## 📊 Analytics

- Desempenho de seleções.
- Estatísticas de partidas.
- Comparação de jogadores.
- Rankings.
- Análises históricas.
- Indicadores esportivos.

## 📈 Visualização

- Dashboards analíticos.
- Indicadores de desempenho.
- Relatórios estatísticos.
- Bases para Business Intelligence.

---

# 🏗 Arquitetura do Projeto

O projeto segue uma arquitetura baseada em camadas de dados.

```text
FWC_2026/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── curated/
│
├── pipelines/
│
├── scripts/
│
├── notebooks/
│
├── dashboards/
│
└── docs/
```

## Camadas de Dados

| Camada | Descrição |
|----------|----------|
| Raw | Dados brutos coletados das fontes |
| Processed | Dados tratados e normalizados |
| Curated | Dados prontos para consumo analítico |
| Pipelines | Fluxos automatizados de processamento |
| Dashboards | Visualizações e indicadores |
| Notebooks | Exploração e análise dos dados |

---

# 🛠 Tecnologias Utilizadas

## Linguagens

- Python
- SQL

## Processamento de Dados

- Pandas
- NumPy
- Apache Spark
- Apache Airflow

## Bancos de Dados

- PostgreSQL
- MySQL
- SQLite

## Analytics e Visualização

- Power BI
- Tableau
- Matplotlib
- Seaborn

## Controle de Versão

- Git
- GitHub

---

# 📊 Casos de Uso

O projeto possui potencial para análises como:

### Seleções

- Ranking por desempenho.
- Histórico de participações.
- Comparação entre países.
- Evolução em Copas do Mundo.

### Jogadores

- Estatísticas individuais.
- Participação em partidas.
- Evolução ao longo do torneio.
- Indicadores de desempenho.

### Partidas

- Resultados históricos.
- Comparativos entre seleções.
- Estatísticas ofensivas e defensivas.
- Indicadores por fase da competição.

### Business Intelligence

- Dashboards executivos.
- Relatórios esportivos.
- Visualizações analíticas.
- Apoio à tomada de decisão baseada em dados.

---

# ⚙️ Como Executar o Projeto

## 1. Clonar o Repositório

```bash
git clone https://github.com/luisshenri/FWC_2026.git
```

## 2. Acessar o Diretório

```bash
cd FWC_2026
```

## 3. Criar Ambiente Virtual

### Windows/Linux/macOS

```bash
python -m venv venv
```

## 4. Ativar Ambiente

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 6. Executar Pipeline

```bash
python main.py
```

---

# 📚 Conceitos Aplicados

Durante o desenvolvimento são praticados conceitos como:

- Engenharia de Dados.
- ETL e ELT.
- Data Lake.
- Data Analytics.
- Data Visualization.
- Modelagem de Dados.
- Governança de Dados.
- Integração de Dados.
- Versionamento de Código.
- Arquitetura de Dados.

---

# 🧠 Aprendizados Desenvolvidos

Este projeto contribui para a consolidação de conhecimentos em:

- Pipeline de Dados.
- Processamento em larga escala.
- Estruturação de Data Warehouses.
- Manipulação de datasets.
- Construção de dashboards.
- Qualidade de dados.
- Python para Engenharia de Dados.
- SQL avançado.
- Git Flow e gerenciamento de branches.

---

# 📈 Roadmap

## Curto Prazo

- Estruturar pipeline inicial.
- Definir modelo de dados.
- Criar camada de ingestão.

## Médio Prazo

- Implementar transformações automatizadas.
- Criar dashboards analíticos.
- Melhorar qualidade dos dados.

## Longo Prazo

- Integração com APIs esportivas.
- Processamento em tempo real.
- Aplicação de Machine Learning.
- Modelos preditivos para partidas e desempenho.

---

# 🎓 Contexto de Aprendizado

A Copa do Mundo FIFA 2026 foi escolhida como tema do projeto por representar um cenário rico em dados, análises e indicadores.

O desenvolvimento deste projeto permite praticar desde a coleta e tratamento dos dados até sua utilização em análises avançadas, reproduzindo desafios encontrados em projetos reais de Engenharia de Dados e Analytics.

---

# 🏆 Objetivos Profissionais

Este projeto faz parte da evolução profissional do autor nas áreas de:

- Engenharia de Dados
- Data Analytics
- Business Intelligence
- Arquitetura de Dados
- Cloud Computing
- Data Governance
- Machine Learning

---

# 👨‍💻 Autor

**Luis Henrique Santos de Souza**

Analista de Projetos Jr, entusiasta de Engenharia de Dados e desenvolvimento de soluções voltadas à geração de valor através de dados.

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos, estudos, demonstração técnica e construção de portfólio.

A utilização é livre para fins educacionais, pesquisas e aprendizado.
