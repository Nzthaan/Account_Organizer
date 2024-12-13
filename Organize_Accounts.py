import os
import time

# Função para gerar o código ANSI para a cor RGB
def rgb_para_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Função para resetar a cor para o padrão
def resetar_cor():
    return "\033[0m"

# Função para criar o gradiente de cores
def texto_com_gradiente(texto, cor_inicial, cor_final):
    r_inicial, g_inicial, b_inicial = cor_inicial
    r_final, g_final, b_final = cor_final
    texto_colorido = ""
    tamanho_texto = len(texto)
    
    for i, char in enumerate(texto):
        if char == '\n':
            texto_colorido += '\n'
        else:
            proporcao = i / tamanho_texto
            r = int(r_inicial + (r_final - r_inicial) * proporcao)
            g = int(g_inicial + (g_final - g_inicial) * proporcao)
            b = int(b_inicial + (b_final - b_inicial) * proporcao)
            texto_colorido += f"{rgb_para_ansi(r, g, b)}{char}"

    texto_colorido += resetar_cor()  # Reseta a cor no final
    return texto_colorido

# Função para exibir o banner com gradiente de cores
def mostrar_banner():
    cor_inicial = (70, 70, 70)  # Cor inicial (cinza escuro)
    cor_final = (240, 240, 240)  # Cor final (cinza claro)
    
    banner = r'''
                              __
                            .d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  ;
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"            _____              _      _ 
   -(.g$$$$$$$b.              .'              |  __ \            (_)    | |
     ""^^T$$$P^)            .(:               | |  | | __ _ _ __  _  ___| |      
       _/  -"  /.'         /:/;               | |  | |/ _` | '_ \| |/ _ \ |
    ._.'-'`-'  ")/         /;/;               | |__| | (_| | | | | |  __/ |
 `-.-"..--""   " /         /  ;               |_____/ \__,_|_| |_|_|\___|_|
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :\
                           ; 
    '''
    
    print(texto_com_gradiente(banner, cor_inicial, cor_final))  # Aplica o gradiente ao banner

# Função para organizar os dados dos usuários
def organizar_usuarios(entrada, saida):
    with open(entrada, "r") as f:
        linhas = f.readlines()

    usuarios = []
    for i in range(0, len(linhas), 3):  # Processa cada 3 linhas (USER, PASSWORD, e linha extra)
        if linhas[i].startswith("USER:") and linhas[i+1].startswith("PASSWORD:"):
            usuario = linhas[i].split(":")[1].strip()  # Extrai o e-mail
            senha = linhas[i+1].split(":")[1].strip()  # Extrai a senha
            usuarios.append(f"{usuario}:{senha}")
    
    if usuarios:
        with open(saida, "w") as f:
            f.writelines([u + "\n" for u in usuarios])  # Escreve os dados organizados
        return True  # Dados salvos com sucesso
    return False  # Não há dados válidos

# Função para gerar o nome do arquivo de saída
def gerar_nome_arquivo_saida(diretorio, nome="DadosNovos.txt"):
    return os.path.join(diretorio, nome)

# Função para verificar a existência do arquivo de entrada e criar se necessário
def verificar_arquivo_entrada(nome):
    caminho = os.path.join(os.getcwd(), nome)
    if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
        print(f"[ + ] O arquivo '{nome}' não contém dados! Criando arquivo de exemplo...")  # Exibe a mensagem
        criar_arquivo_inicial(nome)  # Cria o arquivo de exemplo
        return False  # Retorna False, indicando que o arquivo foi criado
    return True  # Retorna True, arquivo existe e tem dados

# Função para criar o arquivo inicial com dados de exemplo
def criar_arquivo_inicial(nome):
    conteudo = """# Exemplo de dados:
USER: exemplo@dominio.com
PASSWORD: senha123
USER: outro@dominio.com
PASSWORD: senha456
"""
    with open(nome, "w") as f:
        f.write(conteudo)  # Escreve o conteúdo no arquivo
    print(f"[ + ] Arquivo '{nome}' criado com sucesso!")  # Exibe a mensagem de sucesso

# Função para exibir texto em branco
def exibir_texto_branco(texto):
    print(f"\033[38;2;255;255;255m{texto}\033[0m")  # Exibe texto em branco

def main():
    mostrar_banner()  # Exibe o banner
    entrada = "DadosAntigos.txt"  # Nome do arquivo de entrada
    if not verificar_arquivo_entrada(entrada):  # Verifica se o arquivo existe e não está vazio
        print(f"[ + ] O arquivo '{entrada}' não foi encontrado ou estava vazio, criando arquivo de exemplo.")  # Mensagem
        time.sleep(5)  # Espera 5 segundos antes de fechar
        return
    diretorio = os.path.dirname(os.path.abspath(entrada))  # Obtém o diretório do arquivo
    saida = gerar_nome_arquivo_saida(diretorio)  # Gera o nome do arquivo de saída
    if organizar_usuarios(entrada, saida):  # Organiza os dados
        exibir_texto_branco(f"[ + ] Dados organizados salvos em '{saida}'")  # Exibe o sucesso
    else:
        exibir_texto_branco(f"[ + ] O arquivo '{entrada}' não contém dados válidos.")  # Exibe erro
    time.sleep(5)  # Espera 5 segundos antes de fechar

if __name__ == "__main__":
    main()  # Executa o programa
