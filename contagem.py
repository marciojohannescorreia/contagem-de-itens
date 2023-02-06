import os
import csv

# Função que converte o tamanho em bytes para GB
def get_gb_size(size):
    return size / (1024 ** 3)

# Função que retorna a quantidade de pastas, arquivos e tamanho total do diretório
def get_directory_info(dir_path):
    # Inicializa as variáveis que armazenarão a contagem de pastas e arquivos, e o tamanho total
    folder_count = 0
    file_count = 0
    total_size = 0

    # Loop que percorre o diretório e subdiretórios contando as pastas e arquivos e somando o tamanho dos arquivos
    for root, dirs, files in os.walk(dir_path):
        folder_count += len(dirs)
        file_count += len(files)
        for f in files:
            file_path = os.path.join(root, f)
            total_size += os.stat(file_path).st_size
    
    # Retorna a quantidade de pastas, arquivos e tamanho total em GB
    return folder_count, file_count, get_gb_size(total_size)

def main():
    # Solicita o caminho do diretório a ser analisado
    print("Informe o caminho do diretório que você deseja obter informações. Digite 'exit' para encerrar.")

    # Dicionário que armazenará as informações dos diretórios
    data = {}

    # Loop para ler os caminhos dos diretórios
    while True:
        path = input().strip()

        # Se o usuário digitar 'exit', encerra o loop
        if path == 'exit':
            break
        
        # Chama a função get_directory_info para obter as informações do diretório e adiciona no dicionário data
        folder_count, file_count, size = get_directory_info(path)
        data[path] = {"Pastas": folder_count, "Arquivos": file_count, "Tamanho (GB)": "%.2f GB" % size}

    # Solicita o caminho onde o arquivo CSV será salvo
    save_path = input("Informe o caminho onde você deseja salvar o arquivo CSV: ").strip()
    filename = os.path.join(save_path, "RelatorioQi.csv")

    # Abre o arquivo CSV para escrita e escreve as informações do dicionário data
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Caminho", "Pastas", "Arquivos", "Tamanho (GB)"])
        writer.writeheader()
        for path, values in data.items():
            values["Caminho"] = path
            writer.writerow(values)

if __name__ == '__main__':
    main()