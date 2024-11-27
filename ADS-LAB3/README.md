# Prática 3: Intervalo de Confiança - Avaliação de Algoritmos de Ordenação

- Nesta atividade de laboratório, analisamos o desempenho de três algoritmos de ordenação (quick sort, merge sort e counting sort) em diferentes cenários. O objetivo é calcular métricas estatísticas, como média e intervalo de confiança, para entender o comportamento dos algoritmos em relação ao tempo de execução e a escalabilidade. Além disso, os resultados das simulações são analisados para identificar o melhor algoritmo em diferentes cenários.

## Problema

O programa consiste em um benchmark para comparar o desempenho de algoritmos de ordenação com diferentes tamanhos de entrada e faixas de valores. Ele aceita três parâmetros de entrada:

- Algoritmo de ordenação (QUICK, MERGE, COUNTING).
- Tamanho da entrada (número de elementos do array a ser ordenado).
- Valor máximo (faixa de valores dos números inteiros no array).

A execução segue o seguinte formato:

```bash
# No Linux
java -cp bin MedidorDeOrdenacao <ALGORITMO> <TAMANHO_ENTRADA> <VALOR_MAXIMO>
```

# Questões Selecionadas para Automação (1a, 2a e 2b)

**1. Queremos comparar o desempenho de cada algoritmo de ordenação, medindo o tempo para ordenar arrays de inteiros de certos tamanhos e com diferentes faixas de possíveis valores inteiros.**

a. Realize 30 medições para cada algoritmo (quick, merge, counting) e com base nos dados obtidos calcule, para cada um, quantas vezes cada um deve ser executado (tamanho da amostra) para que se tenha um intervalo de confiança com uma margem de erro menor ou igual a 2%, para um nível de confiança de 95%. Use como parâmetros de entrada um tamanho de entrada de 9300000 (9,3 milhões) e o valor máximo da entrada 930000 (930 mil).

Exemplo:

```bash
java -cp bin MedidorDeOrdenacao quick 9300000 930000
java -cp bin MedidorDeOrdenacao merge 9300000 930000
java -cp bin MedidorDeOrdenacao counting 9300000 930000
```

**2. Queremos analisar agora como o tempo de ordenação de cada algoritmo varia ao mudarmos a entrada.**

a. Verifique como o tempo de ordenação aumenta ao aumentarmos o tamanho da entrada, para cada algoritmo. Mantenha fixo o valor máximo em 930000 (930 mil) e varie o tamanho da entrada em dois valores: 9300000 (9,3 milhões) e 93000000 (93 milhões). Analise o padrão de aumento do tempo de ordenação de cada algoritmo e indique qual o melhor e o pior em cada cenário, usando a análise de intervalos de confiança. O tamanho da amostra deve ser suficiente para ter uma margem de erro menor ou igual a 2%.

b. Verifique como o tempo de ordenação aumenta ao aumentarmos a faixa de valores de entrada possíveis (ou seja, aumentando valor máximo da entrada). Mantenha o tamanho da entrada fixo em 9300000 (9,3 milhões) e varie o valor máximo de entrada em dois valores: 930000 (930 mil) e 93000000 (93 milhões). Analise o padrão de aumento do tempo de ordenação de cada algoritmo e indique qual o melhor e o pior em cada cenário, usando a análise de intervalos de confiança. O tamanho da amostra deve ser suficiente para ter uma margem de erro menor ou igual a 2%.

### Executando os scripts

```bash
# No Linux
python3 script_q1a.py
```

```bash
# No Linux
python3 script_q2a.py
```

```bash
# No Linux
python3 script_q2b.py
```

## O que os Scripts vão retornar na Saída

- Script: script_q1a.py
  - Os resultados de cada medição serão salvos no diretório results_q1a.
  - Para cada algoritmo, serão criados subdiretórios com arquivos como:

```bash
results_q1a/QUICK/medicao_1.txt
results_q1a/MERGE/medicao_1.txt
results_q1a/COUNTING/medicao_1.txt
```

- Script: script_q2a.py
  - Os resultados de cada simulação serão salvos no diretório results_q2a.
  - Para cada algoritmo e tamanho de entrada, serão criados subdiretórios com arquivos como:

```bash
results_q2a/QUICK_size_9300000/medicao_1.txt
results_q2a/MERGE_size_9300000/medicao_1.txt
results_q2a/COUNTING_size_9300000/medicao_1.txt
```

- Script: script_q2b.py
  - Os resultados de cada simulação serão salvos no diretório results_q2b.
  - Para cada algoritmo e faixa de valores, serão criados subdiretórios com arquivos como:

```bash
results_q2b/QUICK_max_930000/medicao_1.txt
results_q2b/MERGE_max_930000/medicao_1.txt
results_q2b/COUNTING_max_930000/medicao_1.txt
```
