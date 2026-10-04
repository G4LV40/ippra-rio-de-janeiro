# ippra-rio-de-janeiro

Este repositório reúne os dados e o notebook usados para calcular o Índice de Priorização do Programa de Regularização Ambiental (IPPRA). A análise parte de 23 indicadores municipais e organiza os resultados em quatro componentes, que também ajudam a entender as diferentes dimensões por trás da classificação final.
O notebook foi preparado para ser executado no Google Colab, sem configuração de ambiente local. Ao final, ele gera tabelas em CSV, um gráfico da análise paralela e um arquivo ZIP com os resultados.
Abrir no Google Colab
1. Envie Analise_IPPRA_Colab.ipynb e dataset_IPPRA.xlsx para o Google Drive ou abra o notebook pelo Colab.
2. Execute as células na ordem, ou selecione Ambiente de execução → Executar tudo.
3. Quando solicitado, escolha a planilha dataset_IPPRA.xlsx. Ela deve conter a aba Dados.
4. Ao final, baixe o arquivo resultados_ippra.zip gerado pelo notebook.
A planilha de entrada não é alterada pelo processo. O notebook inclui explicações das etapas e comentários no código.
O que a análise faz
A análise foi realizada com 90 registros municipais e estas 23 variáveis:
qi04, qa04, piaf, poea_af, idhm_e, idhm_l, idhm_r, gin, t_banagua, t_luz, assoc, icms_t, pr_af, exis, pap_pi, pap_us, pap_m, pipo, rlt, appt, aurt, bpm e reg.
As variáveis são padronizadas em escores z. Em seguida, o notebook calcula KMO e MSA, aplica o teste de esfericidade de Bartlett e realiza a análise de componentes principais com rotação Varimax. A quantidade de componentes é definida pela análise paralela, com 1.000 simulações e semente aleatória fixa em 42.
Os escores dos componentes são combinados no Índice Bruto (GI), usando como pesos as respectivas proporções da variância rotacionada. O GI é então reescalado para formar o IPPRA, de 0 a 100. Os registros também são agrupados em quartis: Q1 reúne os menores valores e Q4, os maiores.
Siglas repetidas na planilha representam registros distintos. Para mantê-los separados, o notebook acrescenta sufixos aos identificadores repetidos, como CAB e CAB_1.
Principais resultados
- KMO geral: 0,697.
- Teste de Bartlett: χ²(253) = 1.234,996; p < 0,001.
- Componentes retidos pela análise paralela: 4.
- Variância total explicada pelos quatro componentes: 57,71%.
- GI: de −4,212 a 8,985.
- IPPRA: de 0 a 100.
Três variáveis apresentaram MSA individual abaixo de 0,50: pap_m (0,403), t_banagua (0,415) e reg (0,491). Elas foram mantidas para preservar o conjunto de 23 indicadores definido para o estudo; os resultados associados a essas variáveis devem ser interpretados com cautela.
Arquivos do repositório
- Analise_IPPRA_Colab.ipynb: notebook com o fluxo completo da análise.
- dataset_IPPRA.xlsx: planilha de entrada com os 90 registros e os 23 indicadores.
- requirements.txt: dependência para leitura da planilha fora do Colab.
Arquivos gerados
O ZIP produzido pelo notebook contém, entre outros resultados:
- dados_municipais.csv e estatisticas_descritivas.csv;
- matriz_correlacoes.csv e kmo_msa.csv;
- autovalores_e_retencao.csv e cargas_comunalidades.csv;
- escores_fatoriais.csv, pesos_fatores.csv e indice_ippra.csv;
- limites_gi.csv, com o GI e os limites dos escores fatoriais de cada registro;
- scree_analise_paralela.png e resumo_execucao.json.
O arquivo JSON registra os parâmetros centrais, as versões das bibliotecas e a identificação da planilha usada. A semente 42 controla as simulações da análise paralela; os demais cálculos são determinísticos para os mesmos dados e versões das bibliotecas.
