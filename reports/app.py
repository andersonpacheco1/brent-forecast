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
    with open(os.path.join(base_path, "preco_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    st.subheader("Tendência")
    st.markdown("""
    Este gráfico mostra a tendência de longo prazo nos preços, removendo ruídos e variações 
    sazonais para facilitar a análise de ciclos de alta e baixa.
    O gráfico nos indica que no geral há uma tendência de alta para os preços do petróleo Brent, porém com algumas quedas fortes e repentinas, principalmente a partir de 2011.
    """)
    with open(os.path.join(base_path, "tendencia_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    st.subheader("Sazonalidade")
    st.markdown("""
    Aqui são exibidos os padrões sazonais do preço do petróleo Brent, destacando repetições em 
    certos períodos, como meses ou estações do ano.
    O fato de a sazonalidade do preço do Petróleo Brent variar entre -4 e 2,5 sugere que há uma flutuação periódica nas variações sazonais, com os preços tendendo a cair em certos 
    períodos e subir (valores positivos) em outros. Esses valores indicam que, ao longo do tempo, há momentos em que o preço do petróleo segue padrões de aumento ou diminuição, 
    possivelmente relacionados a fatores sazonais, como mudanças na demanda em diferentes épocas do ano, ajustes de oferta por produtores, ou influências externas como eventos 
    climáticos ou crises econômicas.
    """)
    with open(os.path.join(base_path, "sazonalidade_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

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
    with open(os.path.join(base_path, "residuos_petroleo_brent.html"), "r") as f:
        st.components.v1.html(f.read(), height=500)

    st.subheader('Análise Geopolítica')
    st.write("""
    Os grandes eventos geopolíticos têm um impacto significativo no preço do Petróleo Brent, uma vez que afetam diretamente a oferta e demanda do mercado global. 
    Esses eventos podem ser conflitos armados, embargos, revoluções, ou até negociações de paz entre países produtores de petróleo, o que pode causar uma interrupção na produção ou no transporte de petróleo.
    Com isso, o preço do petróleo pode experimentar grandes flutuações, dependendo da gravidade e da duração desses eventos.
    """)

    st.subheader('Impacto dos Grandes Eventos Geopolíticos no Preço do Petróleo Brent')
    st.write("""
    O gráfico abaixo mostra a relação entre os maiores eventos geopolíticos e o preço do Petróleo Brent. 
    Como pode ser observado, as variações mais expressivas começaram a ocorrer a partir dos anos 2000, com os maiores eventos provocando aumentos significativos no preço do petróleo.
    """)
    image1 = Image.open(os.path.join(base_path, "preco_petroleo_brent_com_eventos_geopoliticos.png"))
    st.image(image1, caption='Preço do Petróleo Brent com Grandes Eventos Geopolíticos')

    st.write("""
    Ao que tudo indica, conforme visto no gráfico acima, os maiores eventos geopolíticos tendem a causar grandes variações no preço, principalmente a partir dos anos 2000, onde as variações parecem ser cada vez mais expressivas.
    """)

    st.subheader('Impacto dos Eventos Geopolíticos nas Regiões Produtoras de Petróleo')
    st.write("""
    O gráfico abaixo foca apenas nos eventos que afetam diretamente os países produtores de petróleo, e parece ter uma correlação ainda mais forte com as variações nos preços do petróleo Brent.
    Esses eventos têm um impacto direto na produção e oferta do petróleo, provocando flutuações mais intensas e rápidas no preço.
    """)
    image2 = Image.open(os.path.join(base_path, "preco_petroleo_brent_com_eventos_produtores.png"))
    st.image(image2, caption='Preço do Petróleo Brent com Eventos em Países Produtores')

with modelos:
    st.subheader('Modelos de Previsão')
    st.write("""
    Para prever o preço do petróleo Brent no futuro, foram utilizados três modelos distintos: 
    o Naive, AutoARIMA e Prophet, sendo que cada um foi testado e avaliado conforme seu desempenho nos dados históricos.
    """)
    st.write("""
    ### Naive Model
    O modelo Naive é o mais simples, assumindo que o valor futuro será igual ao valor mais recente. 
    Apesar de ser útil em ambientes com pouca variação, o modelo tem limitações quando há tendências ou sazonalidade nos dados.
    """)
    st.write("""
    ### AutoARIMA
    O modelo AutoARIMA é mais sofisticado, ajustando-se automaticamente para encontrar o melhor modelo ARIMA (AutoRegressive Integrated Moving Average) para os dados. 
    Ele foi eficaz na captura de tendências e padrões sazonais, mas ainda carece de flexibilidade para lidar com eventos externos de grande impacto.
    """)
    st.write("""
    ### Prophet
    O modelo Prophet é o mais avançado, desenvolvido pela equipe do Facebook para lidar com séries temporais complexas. 
    Ele consegue capturar padrões sazonais e tendências com grande precisão, além de ser altamente configurável para incorporar efeitos de eventos externos.
    O modelo Prophet se mostrou o mais eficiente na previsão do preço do petróleo Brent.
    """)

    st.subheader('Comparação de Modelos')
    image3 = Image.open(os.path.join(base_path, "observada.png"))
    st.image(image3, caption='Observada')

    image4 = Image.open(os.path.join(base_path, "tendencia.png"))
    st.image(image4, caption='Tendência')

    image5 = Image.open(os.path.join(base_path, "sazonalidade.png"))
    st.image(image5, caption='Sazonalidade')

    image6 = Image.open(os.path.join(base_path, "residuos.png"))
    st.image(image6, caption='Resíduos')