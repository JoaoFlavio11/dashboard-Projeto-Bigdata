# Dashboard de Gerenciamento de Estoque

## Introdução
Repositório destinado ao desenvolvimento de um Dashboard para o Trabalho Prático 2 da disciplina: GESTÃO DE DADOS, BIG DATA E DATA MINING.

## Objetivos do Trabalho Prático 2
Responder às Questões Estratégicas (Necessidades de Informação por Indicadores) do Negócio por meio da criação de um Dashboard com Gráficos de Indicadores (dados cuja fonte é o Data Warehouse).

## Descrição Geral do Aplicativo
O projeto consiste em um Dashboard de Gerenciamento de Estoque, que permite aos usuários visualizar e analisar dados relacionados à logistica de um Supermercado. O aplicativo é dividido em três páginas principais:

### Página 1: Gráficos de Gerenciamento de Estoque
Nesta página, são exibidos gráficos interativos que mostram informações sobre o valor de entrada e saída de produtos, armazéns, fornecedores e ao longo do tempo.

### Página 2: Tabelas de Gerenciamento de Estoque
Nesta página, são exibidas tabelas com os dados brutos relacionados ao estoque, incluindo informações sobre fornecedores, locais, produtos, tempo e finanças.

### Página 3: Tabelas Filtradas do Estoque
Nesta página, os usuários podem aplicar filtros aos dados brutos para visualizar apenas as informações relevantes. As tabelas filtradas são exibidas juntamente com um resumo estatístico dos dados.

## Organização dos Arquivos
- **app/pages/**: Contém os scripts Python para cada página do aplicativo.
  - **1-dashboard.py**: Código da 1ª página, que exibe os gráficos de gerenciamento de estoque.
  - **2-Tabelas.py**: código da 2º página, que exibe as tabelas de gerenciamento de estoque.
  - **3-Filtros-para-Tabelas.py**: Código da 3ª página, que permite aos usuários aplicar filtros às tabelas de dados.
- **data/**: Contém os arquivos CSV com os dados brutos do estoque, incluindo informações sobre fornecedores, locais, produtos, tempo e finanças.

