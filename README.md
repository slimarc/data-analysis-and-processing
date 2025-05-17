# 📊 Data Analysis and Processing - Iris Dataset

Este repositório contém a solução prática de uma **atividade acadêmica da disciplina de Inteligência Artificial da UFBA**, que tem como objetivo aplicar técnicas fundamentais de **análise e preparação de dados** utilizando o clássico conjunto de dados **Iris**.

## 🎯 Objetivo

O propósito deste projeto é reforçar os conceitos relacionados a **análise exploratória de dados (EDA)** e **pré-processamento**, preparando o dataset para uso em algoritmos de Machine Learning.

## 📝 Descrição da Atividade

As etapas realizadas neste projeto seguem as diretrizes propostas na prática da disciplina e incluem:

1. **Carregamento do Dataset**  
   - Utilização da biblioteca `seaborn` para importar o dataset Iris.
   
2. **Análise Inicial dos Dados**  
   - Visualização das primeiras linhas.
   - Verificação da estrutura e dos tipos de dados.

3. **Tratamento de Dados Ausentes**  
   - Checagem por valores nulos.
   - Aplicação de técnicas de imputação ou remoção quando necessário (com justificativa).

4. **Identificação e Tratamento de Outliers**  
   - Construção de boxplots para análise de dispersão.
   - Estratégias de remoção ou ajuste dos valores discrepantes.

5. **Análise Exploratória (EDA)**  
   - Geração de **pelo menos 3 gráficos relevantes**, como histogramas, gráficos de contagem e mapa de correlação.
   - Análise dos padrões e insights encontrados nos dados.

6. **Normalização dos Dados**  
   - Aplicação do `StandardScaler` para normalização das colunas numéricas.

7. **Exportação do Dataset Tratado**  
   - Salvamento do novo arquivo tratado como `iris_tratada.csv`.

## 📁 Estrutura do Repositório

```bash
data-analysis-and-processing/
│
├── 📁 graphics/                      # Imagens dos gráficos gerados durante a análise
│   ├── boxplot_example.png
│   ├── histogram.png
│   └── correlation_heatmap.png
└── 📄 processing_iris.csv            # Arquivo com os dados tratados e normalizados
                  
