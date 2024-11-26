import os
import subprocess

OUTPUT_DIR = "results_questao2"
TEMPO_SERVICO = 0.84
NUM_SERVIDORES = 10
TEMPO_OBSERVACAO = 30
TAXAS_CHEGADA = [5, 10, 15, 20, 25, 30]  # Modifique se necessário

# Criar diretório de saída
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_simulation(taxa_chegada):
   
    print(f"Executando com Taxa de Chegada: {taxa_chegada}, "
          f"Tempo de Serviço: {TEMPO_SERVICO}, "
          f"Servidores: {NUM_SERVIDORES}, "
          f"Tempo de Observação: {TEMPO_OBSERVACAO}...")
    
    output_file = os.path.join(OUTPUT_DIR, f"taxa-{taxa_chegada}.txt")
    
    # Comando Java
    command = [
        "java", "-cp", "bin:lib/*", "ServidorWeb",
        str(taxa_chegada), str(TEMPO_SERVICO), str(NUM_SERVIDORES), str(TEMPO_OBSERVACAO)
    ]

    with open(output_file, "w") as f:
        subprocess.run(command, stdout=f)
    
    print(f"Resultados salvos em: {output_file}")

for taxa in TAXAS_CHEGADA:
    run_simulation(taxa)

print(f"Simulações concluídas! Resultados disponíveis em {OUTPUT_DIR}.")
