import os
import subprocess


BASE_OUTPUT_DIR = "results_q1a"
TAMANHO_ENTRADA = 9300000
VALOR_MAXIMO = 930000
ALGORITMOS = ["QUICK", "MERGE", "COUNTING"]
NUM_MEDICOES = 30

os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)

def executar_medicao(algoritmo, tamanho_entrada, valor_maximo, medicao_num, output_dir):
    comando = [
        "java",
        "-cp", "bin",
        "MedidorDeOrdenacao",
        algoritmo,
        str(tamanho_entrada),
        str(valor_maximo)
    ]
    with open(os.path.join(output_dir, f"medicao_{medicao_num}.txt"), "w") as output_file:
        subprocess.run(comando, stdout=output_file)

# Loop pelos algoritmos
for algoritmo in ALGORITMOS:
    algoritmo_dir = os.path.join(BASE_OUTPUT_DIR, algoritmo)
    os.makedirs(algoritmo_dir, exist_ok=True)
    print(f"Executando {NUM_MEDICOES} medições para o algoritmo: {algoritmo}")

    for i in range(1, NUM_MEDICOES + 1):
        print(f"Medição {i} para {algoritmo}...")
        executar_medicao(algoritmo, TAMANHO_ENTRADA, VALOR_MAXIMO, i, algoritmo_dir)

    print(f"Resultados para {algoritmo} salvos no diretório {algoritmo_dir}")

print(f"Medições concluídas! Resultados disponíveis no diretório {BASE_OUTPUT_DIR}.")
