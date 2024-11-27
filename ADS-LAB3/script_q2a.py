import os
import subprocess

# Definir configurações
BASE_OUTPUT_DIR = "results_q2a"
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)

VALOR_MAXIMO = 930000
TAMANHOS_ENTRADA = [9300000, 93000000]
N = 50  # Número de medições
ALGORITMOS = ["QUICK", "MERGE", "COUNTING"]

# Loop para executar as medições
for tamanho_entrada in TAMANHOS_ENTRADA:
    for algoritmo in ALGORITMOS:
        algoritmo_dir = os.path.join(BASE_OUTPUT_DIR, f"{algoritmo}_size_{tamanho_entrada}")
        os.makedirs(algoritmo_dir, exist_ok=True)

        print(f"Executando {N} medições para {algoritmo} com tamanho de entrada {tamanho_entrada} e valor máximo {VALOR_MAXIMO}")
        
        for i in range(1, N + 1):
            print(f"Medição {i} para {algoritmo} com tamanho de entrada {tamanho_entrada}...")
            
            # Executar o comando Java
            comando = [
                "java", "-cp", "bin:.", "MedidorDeOrdenacao", 
                algoritmo, str(tamanho_entrada), str(VALOR_MAXIMO)
            ]
            with open(os.path.join(algoritmo_dir, f"medicao_{i}.txt"), "w") as output_file:
                subprocess.run(comando, stdout=output_file)

        print(f"Resultados para {algoritmo} com tamanho de entrada {tamanho_entrada} salvos no diretório {algoritmo_dir}")

print(f"Medições concluídas! Resultados disponíveis no diretório {BASE_OUTPUT_DIR}.")
