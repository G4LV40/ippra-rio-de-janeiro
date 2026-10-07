Este repositório reúne os dados, o notebook e o script usados nas análises do Índice de Priorização do Programa de Regularização Ambiental (IPPRA). A análise principal parte de 23 indicadores municipais e organiza os resultados em quatro componentes, que ajudam a compreender as dimensões por trás da classificação final.
O notebook foi preparado em Python, sem configuração de ambiente local. Ao final, gera tabelas em CSV, um gráfico da análise paralela e um arquivo ZIP com os resultados.
O notebook contém explicações das etapas e comentários no código.
O que a análise faz:
A análise principal foi realizada com 90 registros municipais e estas 23 variáveis: qi04, qa04, piaf, poea_af, idhm_e, idhm_l, idhm_r, gin, t_banagua, t_luz, assoc, icms_t, pr_af, exis, pap_pi, pap_us, pap_m, pipo, rlt, appt, aurt, bpm e reg.
As variáveis são padronizadas em escores z. Em seguida, o notebook calcula KMO e MSA, aplica o teste de esfericidade de Bartlett e realiza a análise de componentes principais com rotação Varimax. A quantidade de componentes é definida pela análise paralela, com 1.000 simulações e semente aleatória fixa em 42.
Os escores dos componentes são combinados no Índice Bruto (GI), usando como pesos as respectivas proporções da variância rotacionada. O GI é reescalado para formar o IPPRA, de 0 a 100. Os registros também são agrupados em quartis: Q1 reúne os menores valores e Q4, os maiores.
Siglas repetidas na planilha representam registros distintos. Para mantê-los separados, o notebook acrescenta sufixos aos identificadores repetidos, como CAB e CAB_1.
Principais resultados
- KMO geral: 0,697.
- Teste de Bartlett: χ²(253) = 1.234,996; p < 0,001.
- Componentes retidos pela análise paralela: 4.
- Variância total explicada pelos quatro componentes: 57,71%.
- GI: de −4,212 a 8,985.
- IPPRA: de 0 a 100.
Arquivos do repositório
- Analise_IPPRA_.ipynb: notebook com o fluxo completo da análise principal.
- dataset_IPPRA.xlsx: planilha de entrada com os 90 registros e os 23 indicadores.
- crosswalk_municipios_IPPRA_1.xlsx: planilha de correspondência municipal que documenta a relação entre os identificadores usados no estudo.
- sensitivity_analysis.py: script para reproduzir a análise de sensibilidade do GI apresentada na Tabela S1 do Material Suplementar.
