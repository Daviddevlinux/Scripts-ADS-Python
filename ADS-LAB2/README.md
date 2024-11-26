# Prática 2: Teoria das Filas / Simulação - Avaliação de Desempenho de Sistemas

- Nesta atividade de laboratório é apresentado um problema de teoria das filas, envolvendo um simulador de um sistema web. Você deve executar o programa fornecido e avaliar o desempenho do mesmo, a partir das métricas gravadas pelo programa. Você também deve aplicar os conceitos de teoria das filas para resolver as questões de forma analítica. Para responder às questões, você deve escrever um relatório com as suas análises.

## Problema

O programa deste laboratório é um simulador de um sistema Web, que possui n servidores para processar as A0 requisições realizadas no tempo de observação T escolhido. Para executá-lo, você precisa passar a seguinte sequência de parâmetros:

```bash
# No Linux
java -cp bin:lib/* ServidorWeb <taxa-de-chegada-media> <tempo-de-servico-medio> <num-servidores> <tempo-observacao>
```

## Os parâmetros de entrada do programa são:

**1.** Taxa de chegada de requisições que são realizadas para o sistema web, em requisições por segundo.

**2.** Tempo médio de serviço para o processamento de uma requisição, em segundos.

**3.** Número de servidores (n) que serão usados para processar as requisições. Na implementação, cada servidor é uma thread do sistema, sendo possível processar até n requisições simultaneamente no sistema web.

**4.** Tempo durante o qual o sistema web será observado e medido na simulação.

### Como saída, a execução do programa vai gerar as seguintes saídas na tela:

- TaxaDeChegadaMedia: o valor do parâmetro de taxa de chegada média de requisições, que foi passado como entrada.
- TempoDeServicoMedio: o valor do parâmetro de tempo serviço médio de requisições, que foi passado como entrada.
- NumServidores: o valor do parâmetro de número de servidores, que foi passado como entrada.
- RequisicoesSubmetidas: quantidade de requisições que foram submetidas (ou seja, que chegaram) ao servidor web durante o tempo de observação.
- RequisicoesConcluidas: quantidade de requisições que foram finalizadas (ou seja, completaram sua execução) durante o tempo de observação.
- TempoMedioDeResposta: tempo médio de resposta para as requisições executadas no servidor web.
- TamanhoMedioDaFila: tamanho médio da fila de requisições acumuladas no sistema web durante a execução.

**Você deve responder às questões abaixo explorando diferentes configurações de parâmetros de entrada, analisando as saídas e usando as técnicas de modelagem analítica (teoria das filas) aprendidas na disciplina.**

# Questões Selecionadas para Automação (2 e 3)

**2. Como o tempo de resposta das requisições varia ao aumentar a carga do sistema (ou seja, aumentar a taxa de chegada de requisições no sistema)? Você considera esse sistema web escalável? Considere para esta questão o seguinte cenário base de parâmetros de entrada:**

- Taxa de chegada: variável
- Tempo de serviço: 0.84 segundo
- Número de servidores: 10
- Tempo de observação: 30 segundos

**3. Qual a quantidade mínima de servidores necessários para obter um tempo de resposta médio menor que 1 segundo? Analise diferentes cenários de simulação para dar sua resposta. Considere para esta questão o seguinte cenário base de parâmetros de entrada:**

- Taxa de chegada: 9,5 requisições por segundo
- Tempo de serviço: 0.84 segundo
- Número de servidores: variável
- Tempo de observação: 30 segundos

### Executando o script Python

```bash
# No Linux
python3 script_questao2.py
```

### O que o Script vai retornar de Saída

- Os resultados de cada simulação serão salvos no diretório results_questao2.
- Você verá vários arquivos dentro do diretório que estarão dessa forma:

```bash
results_questao2/taxa-5.txt
results_questao2/taxa-10.txt
results_questao2/taxa-15.txt
```

### **Cada arquivo contém:**

- Taxa média de chegada de requisições.
- Tempo médio de resposta.
- Quantidade de requisições submetidas e concluídas.
- Tamanho médio da fila durante a simulação.

---

### Executando o script Python

```bash
# No Linux
python3 script_questao3.py
```

### O que o Script vai retornar de Saída

- Os resultados de cada simulação serão salvos no diretório results_questao3.
- Você verá vários arquivos dentro do diretório que estarão dessa forma:

```bash
results_questao3/servers-1.txt
results_questao3/servers-2.txt
results_questao3/servers-3.txt
```

### **Cada arquivo contém:**

- Taxa média de chegada de requisições.
- Tempo médio de resposta.
- Quantidade de requisições submetidas e concluídas.
- Tamanho médio da fila durante a simulação.
