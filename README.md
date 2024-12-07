# Tech Challenge - Análise e Previsão de Preços do Petróleo Brent

## Contexto

Este projeto foi desenvolvido no âmbito do **Tech Challenge**, uma atividade obrigatória que integra os conhecimentos adquiridos ao longo do curso. O desafio consistia em realizar uma consultoria para um grande cliente do segmento de petróleo, analisando dados históricos de preços do petróleo Brent e gerando insights relevantes para a tomada de decisão.

## O Problema

A tarefa principal envolvia a análise de uma base de dados histórica contendo dois campos: **data** e **preço** do petróleo Brent, encontrados no site do IPEA. A consultoria deveria desenvolver um **dashboard interativo** para gerar insights e, além disso, criar um **modelo de Machine Learning** para prever o preço futuro do petróleo Brent.

## Objetivos

1. **Analisar os dados históricos de preço do petróleo Brent**: Identificar padrões e tendências no comportamento do preço.
2. **Desenvolver modelos de previsão de preço**: Comparar modelos como Naive, AutoARIMA e Prophet.
3. **Criar um dashboard interativo**: Exibir as previsões e insights gerados para os tomadores de decisão.

## Resultados Finais

### Análise de Dados
Durante o desenvolvimento do projeto, foi realizada uma análise aprofundada dos preços históricos do petróleo Brent, incluindo:
- O impacto de **eventos geopolíticos** no preço do petróleo.
- A **sazonalidade** no preço do Brent.

### Modelos de Previsão
Três modelos de previsão foram avaliados:

1. **Naive**: Modelo simples, que utiliza o valor mais recente como previsão para os próximos períodos. Serve como uma referência inicial, mas não captura tendências complexas.
   
2. **AutoARIMA**: Um modelo mais avançado que tenta capturar tendências e sazonalidade nos dados. Apresenta melhorias em relação ao Naive, mas ainda é sensível a grandes variações em períodos curtos.
   
3. **Prophet**: Modelo robusto que captura tendências e sazonalidade de forma mais eficaz. Foi o modelo que apresentou os melhores resultados em termos de precisão e consistência.

### Dashboard Interativo
O dashboard interativo desenvolvido utiliza o modelo **Prophet** para fornecer previsões de preços do petróleo Brent, além de permitir a visualização de tendências, sazonalidade e impacto de eventos geopolíticos.

## Conclusões

- **Naive** e **AutoARIMA** mostraram-se adequados para análises preliminares, mas **Prophet** superou ambos ao reduzir significativamente os erros e proporcionar previsões mais confiáveis.
- O **dashboard interativo** oferece uma ferramenta útil para os tomadores de decisão, proporcionando insights sobre os fatores que afetam o preço do petróleo.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas: `streamlit`, `prophet`, `statsmodels`, `pandas`, `numpy`, `matplotlib`, `plotly`, entre outras.

### Passos para rodar

1. Clone este repositório:

    ```bash
    git clone https://github.com/usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o aplicativo Streamlit:

    ```bash
    streamlit run app.py
    ```

## Leitura Relevante

Se você deseja se aprofundar mais sobre os temas abordados no projeto, abaixo estão algumas sugestões de leitura:

- **"The Economics of Oil"** de James Smith: Uma análise detalhada sobre os fatores que influenciam o preço do petróleo.
- **"Oil and Geopolitics"** de Kenneth B. Medlock III: Este livro explora como os eventos geopolíticos moldam o mercado global de petróleo.
- **Documentação do Prophet**: [Prophet Documentation](https://facebook.github.io/prophet/docs/forecaster.html)
- **ARIMA e AutoARIMA**: [ARIMA Models and Time Series Analysis](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.