import os

def ler_ppm_ascii(nome_arquivo):
    matriz = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        # Ignorar cabeçalho
        linhas = linhas[3:]
        for linha in linhas:
            # Remover espaços em branco extras e quebrar a linha em valores individuais
            valores = linha.strip().split()
            # Converter os valores de string para inteiros
            valores = [int(valor) for valor in valores]
            matriz.append(valores)
    return matriz
    
def salvar_ppm_ascii(matriz, largura, altura, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        # Escrever o cabeçalho
        arquivo.write("P2\n")
        arquivo.write(f"{largura} {altura}\n")
        arquivo.write("255\n")
        
        # Escrever os valores da matriz
        for linha in matriz:
            for valor in linha:
                arquivo.write(f"{valor} ")
            arquivo.write("\n")
            
def rodar_sem():
	for i in range(5):
	  print(i)

# Obter o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo na mesma pasta que o script
nome_arquivo = os.path.join(diretorio_atual, 'pimentoes.pgm')

matriz_imagem = ler_ppm_ascii(nome_arquivo)
print(matriz_imagem)

nome_arquivo1 = os.path.join(diretorio_atual, 'imagem.pgm')

largura = 512
altura = 512
print(largura,altura)
salvar_ppm_ascii(matriz_imagem, largura, altura, nome_arquivo1)
