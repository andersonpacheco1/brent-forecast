import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from PIL import Image

st.title('Brent Forecast')

# Caminho absoluto para os arquivos
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reports', 'figures'))

resumo ,eda, modelos = st.tabs(['Resumo', 'Comportamento e Análise Geopolítica', 'Modelos'])

with resumo:
    st.subheader('Resumo')

    st.title('Resumo Geral do Tech Challenge')

    st.write("""
    ### Contexto
    Este projeto foi desenvolvido no âmbito do **Tech Challenge**, uma atividade obrigatória que integra os conhecimentos adquiridos ao longo do curso. O desafio consistia em realizar uma consultoria para um grande cliente do segmento de petróleo, analisando dados históricos de preços do petróleo Brent e gerando insights relevantes para a tomada de decisão.

    ### O Problema
    A tarefa principal envolvia a análise de uma base de dados histórica contendo dois campos: **data** e **preço** do petróleo Brent, encontrados no site do IPEA. A consultoria deveria desenvolver um **dashboard interativo** para gerar insights e, além disso, criar um **modelo de Machine Learning** para prever o preço futuro do petróleo Brent.

    A seguir, é apresentado um resumo dos resultados alcançados e as conclusões gerais sobre o desenvolvimento do dashboard e dos modelos de previsão.
    """)

    st.write("""
    ### Resultados Finais e Conclusões
    Durante o desenvolvimento do projeto, foi realizada uma análise aprofundada dos preços históricos do petróleo Brent, incluindo o comportamento dos preços ao longo do tempo e a identificação de fatores que afetam essas flutuações, como **eventos geopolíticos** e **sazonalidade**.

    Foram aplicados e comparados três modelos de previsão de preços do petróleo Brent:
    1. **Naive**: O modelo mais simples, que utiliza o valor mais recente como previsão para os próximos períodos. Embora útil para fornecer uma referência inicial, apresenta limitações, principalmente em relação à incapacidade de capturar variações mais complexas.
    2. **AutoARIMA**: Um modelo mais avançado, que tenta capturar tendências e sazonalidade nos dados. Apesar de apresentar melhorias em relação ao Naive, ainda se mostrou sensível a grandes variações em períodos curtos.
    3. **Prophet**: O modelo mais eficaz, capaz de capturar as tendências e padrões sazonais de maneira robusta. Demonstrou uma redução significativa nos erros e foi considerado o mais indicado para a previsão do preço do petróleo Brent.

    O modelo **Prophet** foi o mais preciso e consistente entre os avaliados, sendo o escolhido para integrar o dashboard interativo, que permite ao cliente obter previsões mais confiáveis para os preços futuros do petróleo.

    Além disso, o dashboard interativo desenvolvido permite visualizar as tendências, sazonalidade e grandes eventos geopolíticos que impactam o preço do Brent, ajudando os tomadores de decisão a antecipar mudanças no mercado.

    O trabalho final foi entregue com sucesso, atendendo aos requisitos do cliente, e os resultados alcançados demonstraram o valor das ferramentas de **Machine Learning** e **análise de séries temporais** no contexto do mercado de petróleo.
    """)

with eda:
    st.subheader('Comportamento dos Dados')

    # Preço do Petróleo Brent
    st.subheader("Preço do Petróleo Brent")
    st.markdown("""
    O Petróleo Brent é uma das principais referências globais para precificação de petróleo. 
    Extraído do Mar do Norte, ele é amplamente utilizado como benchmark nos mercados financeiros 
    para contratos futuros de petróleo, sendo essencial na determinação de preços internacionais 
    de energia.

    Historicamente, o preço do petróleo Brent é influenciado por diversos fatores, como:
    - **Geopolítica**: Conflitos em regiões produtoras, como Oriente Médio, frequentemente causam variações nos preços.
    - **Oferta e Demanda**: A produção da OPEP (Organização dos Países Exportadores de Petróleo) e o consumo global impactam diretamente os valores.
    - **Fatores Econômicos**: Crescimento econômico, crises financeiras e até políticas ambientais alteram a dinâmica de preços.

    Este gráfico permite visualizar as mudanças ao longo do tempo, ajudando a identificar períodos 
    de alta volatilidade ou estabilidade no mercado. Ele é essencial para compreender como eventos 
    históricos e mudanças estruturais no setor energético afetaram o preço do petróleo.
    """)
    with open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "preco_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    # Tendência
    st.subheader("Tendência")
    st.markdown("""
    Este gráfico mostra a tendência de longo prazo nos preços, removendo ruídos e variações 
    sazonais para facilitar a análise de ciclos de alta e baixa.
    O gráfico nos indica que no geral a uma tendência de alta para os preços do petróleo Brent, porém com algumas quedas fortes e repentinas principalmente a partir de 2011.
    """)
    with open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "tendencia_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    # Sazonalidade
    st.subheader("Sazonalidade")
    st.markdown("""
    Aqui são exibidos os padrões sazonais do preço do petróleo Brent, destacando repetições em 
    certos períodos, como meses ou estações do ano.
    O fato de a sazonalidade do preço do Petróleo Brent variar entre -4 e 2,5 sugere que há uma flutuação periódica nas variações sazonais, com os preços tendendo a cair em certos 
    períodos e subir (valores positivos) em outros. Esses valores indicam que, ao longo do tempo, há momentos em que o preço do petróleo segue padrões de aumento ou diminuição, 
    possivelmente relacionados a fatores sazonais, como mudanças na demanda em diferentes épocas do ano, ajustes de oferta por produtores, ou influências externas como eventos 
    climáticos ou crises econômicas.
    """)
    with open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "sazonalidade_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    # Resíduos
    st.subheader("Resíduos")
    st.markdown("""
    Os resíduos representam as discrepâncias entre os valores reais e os valores ajustados pelo 
    modelo de decomposição.
    As discrepâncias nos resíduos do preço do petróleo Brent representam as diferenças entre os valores reais e os ajustados pelo modelo. Elas podem indicar:
    1. *Eventos anômalos*: Choques externos como crises, guerras ou mudanças na oferta/demanda.
    2. *Falhas no modelo*: Tendências ou sazonalidades não capturadas pelo modelo.
    3. *Volatilidade crescente*: Resíduos mais amplos ao longo do tempo podem refletir maior sensibilidade a fatores geopolíticos e econômicos.
    Esses resíduos ajudam a avaliar a qualidade do modelo e identificar períodos de instabilidade no mercado.
    """)
    with open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "residuos_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    st.subheader('Análise Geopolítica')
    # Introdução sobre o impacto dos eventos geopolíticos
    st.write("""
    Os grandes eventos geopolíticos têm um impacto significativo no preço do Petróleo Brent, uma vez que afetam diretamente a oferta e demanda do mercado global. 
    Esses eventos podem ser conflitos armados, embargos, revoluções, ou até negociações de paz entre países produtores de petróleo, o que pode causar uma interrupção na produção ou no transporte de petróleo.
    Com isso, o preço do petróleo pode experimentar grandes flutuações, dependendo da gravidade e da duração desses eventos.
    """)

    # Exibindo o gráfico de eventos geopolíticos gerais
    st.subheader('Impacto dos Grandes Eventos Geopolíticos no Preço do Petróleo Brent')
    st.write("""
    O gráfico abaixo mostra a relação entre os maiores eventos geopolíticos e o preço do Petróleo Brent. 
    Como pode ser observado, as variações mais expressivas começaram a ocorrer a partir dos anos 2000, com os maiores eventos provocando aumentos significativos no preço do petróleo.
    """)
    image1 = Image.open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "preco_petroleo_brent_com_eventos_geopoliticos.png"))
    st.image(image1, caption='Preço do Petróleo Brent com Grandes Eventos Geopolíticos')

    # Texto explicativo sobre o gráfico
    st.write("""
    Ao que tudo indica, conforme visto no gráfico acima, os maiores eventos geopolíticos tendem a causar grandes variações no preço, principalmente a partir dos anos 2000, onde as variações parecem ser cada vez mais expressivas.
    """)

    # Exibindo o gráfico de eventos geopolíticos focados em países produtores
    st.subheader('Impacto dos Eventos Geopolíticos nas Regiões Produtoras de Petróleo')
    st.write("""
    O gráfico abaixo foca apenas nos eventos que afetam diretamente os países produtores de petróleo, e parece ter uma correlação ainda mais forte com as variações nos preços do petróleo Brent.
    Esses eventos têm um impacto direto na produção e oferta do petróleo, provocando flutuações mais intensas e rápidas no preço.
    """)
    image2 = Image.open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "preco_petroleo_brent_com_eventos_produtores.png"))
    st.image(image2, caption='Preço do Petróleo Brent com Eventos Geopolíticos em Regiões Produtoras')

    # Conclusão
    st.write("""
    **Conclusão**: Com base nos gráficos apresentados, fica claro que os eventos geopolíticos, especialmente aqueles que afetam diretamente os países produtores de petróleo, têm uma influência significativa sobre o preço do petróleo Brent. 
    Esses eventos geram incertezas no mercado, o que pode resultar em grandes oscilações de preços, como evidenciado nos gráficos.
    """)

with modelos:
    st.title('Comparação de Modelos para Previsão de Preços do Petróleo Brent')

    # Explicação sobre os modelos
    st.write("""
    Neste estudo, foram avaliados três modelos para prever os preços do petróleo Brent: o modelo Naive, o AutoARIMA e o Prophet. Cada um desses modelos tem características distintas que impactam a acurácia e a capacidade de prever com precisão o comportamento dos preços no futuro.
    """)

    # Explicação sobre o Modelo Naive
    st.write("""
    ### 1. Modelo Naive
    O modelo Naive utiliza o valor mais recente da série temporal como previsão para os próximos períodos. Esse modelo simples é útil como uma referência inicial, mas apresenta algumas limitações, como a incapacidade de capturar tendências ou padrões temporais importantes. Embora o erro absoluto médio (MAE) seja relativamente baixo, o erro quadrático médio (MSE) é maior, refletindo a tendência do modelo em cometer erros maiores em algumas previsões, principalmente em períodos com grande variação nos preços.
    """)

    # Gráfico do Modelo Naive (HTML)
    st.subheader('Previsão com o Modelo Naive')
    st.components.v1.html(open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "previsao_naive_brent.html"), 'r').read(), height=600)

    # Métricas de erro para o Modelo Naive
    st.write("""
    **Métricas de Erro do Modelo Naive:**
    - **MSE (Erro Quadrático Médio)**: 3.68
    - **MAE (Erro Absoluto Médio)**: 1.61

    Como observado, o modelo Naive apresenta um MAE relativamente baixo, mas o MSE é mais elevado, indicando que o modelo comete erros significativos em períodos de grande variação dos preços.
    """)

    # Explicação sobre o Modelo AutoARIMA
    st.write("""
    ### 2. Modelo AutoARIMA
    O modelo AutoARIMA (AutoRegressive Integrated Moving Average) é mais avançado que o Naive, pois tenta identificar automaticamente a melhor combinação de tendências e sazonalidade nos dados. Ele apresenta uma leve melhoria no MAE em relação ao Naive, indicando que o modelo é capaz de capturar as variações de preços com mais precisão. No entanto, o MSE do AutoARIMA é ligeiramente maior que o do Naive, o que sugere que o modelo ainda pode ser sensível a grandes variações nos dados, especialmente em horizontes mais curtos.
    """)

    # Gráfico do Modelo AutoARIMA (HTML)
    st.subheader('Previsão com o Modelo AutoARIMA')
    st.components.v1.html(open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "previsao_autoarima_brent.html"), 'r').read(), height=600)

    # Métricas de erro para o Modelo AutoARIMA
    st.write("""
    **Métricas de Erro do Modelo AutoARIMA:**
    - **MSE (Erro Quadrático Médio)**: 3.90
    - **MAE (Erro Absoluto Médio)**: 1.60

    O AutoARIMA apresenta uma leve melhoria sobre o Naive no MAE, mas o MSE um pouco mais alto indica que o modelo ainda tem dificuldades em capturar variações abruptas e imprevisíveis nos dados.
    """)

    # Explicação sobre o Modelo Prophet
    st.write("""
    ### 3. Modelo Prophet
    O modelo Prophet, desenvolvido pelo Facebook, é uma ferramenta mais robusta para previsão de séries temporais, especialmente quando há tendências sazonais e feriados envolvidos. Ele se destaca significativamente em relação aos outros modelos, com uma melhoria de mais de 50% no MSE em comparação com o AutoARIMA e o Naive. Além disso, o Prophet apresenta o menor MAE entre os modelos avaliados, mostrando que ele é o mais consistente na previsão dos preços do Brent.
    """)

    # Gráfico do Modelo Prophet (HTML)
    st.subheader('Previsão com o Modelo Prophet')
    st.components.v1.html(open(os.path.join(os.path.dirname(__file__), "..", "reports", "figures", "previsao_prophet.html"), 'r').read(), height=600)

    # Métricas de erro para o Modelo Prophet
    st.write("""
    **Métricas de Erro do Modelo Prophet:**
    - **MSE (Erro Quadrático Médio)**: 1.84
    - **MAE (Erro Absoluto Médio)**: 1.05

    O modelo Prophet se destaca com os menores erros de previsão, tanto em MAE quanto em MSE, o que reflete sua capacidade superior em capturar as tendências e padrões sazonais dos preços do petróleo Brent.
    """)

    # Conclusões
    st.write("""
    ### Conclusões:
    - **Naive**: Embora simples, o modelo Naive serve como uma boa referência inicial, mas sofre com erros maiores devido à sua incapacidade de capturar as variações complexas nos dados. 
    - **AutoARIMA**: Apresenta uma leve melhoria sobre o Naive, conseguindo identificar algumas variações sazonais e tendências, mas ainda com sensibilidade a erros maiores.
    - **Prophet**: Se destaca como o modelo mais eficaz, com uma redução significativa nos erros e uma previsão mais consistente. Ele é o mais indicado para prever os preços do petróleo Brent entre os modelos testados.

    A tabela abaixo apresenta as métricas de erro de cada modelo:
    - **MSE (Erro Quadrático Médio)** do Modelo Naive: 3.68
    - **MAE (Erro Absoluto Médio)** do Modelo Naive: 1.61
    - **MSE (Erro Quadrático Médio)** do Modelo AutoARIMA: 3.90
    - **MAE (Erro Absoluto Médio)** do Modelo AutoARIMA: 1.60
    - **MSE (Erro Quadrático Médio)** do Modelo Prophet: 1.84
    - **MAE (Erro Absoluto Médio)** do Modelo Prophet: 1.05
    """)

    # Conclusão Geral
    st.write("""
    ### Conclusão Geral
    Com base nos resultados dos modelos, o **Prophet** se mostra como a melhor opção para prever o preço do petróleo Brent. Sua capacidade de capturar tendências e padrões sazonais, combinada com uma significativa redução nos erros, faz dele o modelo mais indicado entre os avaliados.
    """)