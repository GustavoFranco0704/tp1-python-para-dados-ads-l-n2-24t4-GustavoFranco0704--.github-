import random

# 1 - Aquecendo os motores ⭐

usuarios = [
    ["Ana Silva", 29, "São Paulo", "SP"],
    ["Carlos Pereira", 34, "Rio de Janeiro", "RJ"],
    ["Beatriz Costa", 22, "Curitiba", "PR"],
    ["Daniel Souza", 40, "Belo Horizonte", "MG"],
    ["Fernanda Alves", 27, "Porto Alegre", "RS"],
    ["", 32, "Manaus", "AM"],
    ["Gabriela", 20, "", "PR"]
]

# 2 -  Perfil ⭐⭐

lista_usuarios = []


def dicionario_usuarios():
    for usuario in usuarios:
        perfil = {
            'nome': usuario[0],
            'idade': usuario[1],
            'localizacao': (usuario[2], usuario[3])
        }
        lista_usuarios.append(perfil)
    return lista_usuarios


resultado = dicionario_usuarios()
print("### Perfil ### ")
print(" ")
print(resultado)
print(" ")

# 3 -  Comparando Estruturas ⭐⭐⭐

# A principal diferença entre lista, dicionário e uma tupla são.
# O dicionário armazena dados com chave e valor, ela também e mutável e não ordernada. O dicionario no contexto do INFwebNET é usado para aramazenar os valores com chave e valor, ex: nome: "Ana Silva".
# A tupla armazena valores imutáveis e ordenada, ou seja em sequência. No contexto do INFwebNET ela é utilizada na chave localizacao, com 2 valores que não serão alterados.
# A lista é mutável e ordenada ou seja ela tem valores em sequência. No contexto do INFwebNET ela é utilizada para acessar valores através de indíces para armazenar em um dicionário.

# 4 -  Limpando o terreno ⭐⭐


perfis_validos = []


def verifica_usuarios_validos():
    for usuario in lista_usuarios:
        if usuario.get("nome") and usuario.get("localizacao")[0]:
            perfis_validos.append(usuario)

    return perfis_validos


resultado_validos = verifica_usuarios_validos()
print("### Limpando o terreno ###")
print(" ")
print(resultado_validos)
print(" ")

# 5 - Carregando dados ⭐⭐⭐

perfil_social = []

with open("base_inicial.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        separador = linha.strip().split("?")

        nome = separador[0]
        idade = separador[1]
        localizacao = (separador[2], separador[3])
        amigos = set(separador[4:])

        if nome and localizacao[0]:
            perfil = {
                'nome': nome,
                'idade': idade,
                'localizacao': localizacao,
                'amigos': amigos
            }
            perfil_social.append(perfil)

print(" ### Carregando dados ###")
print(" ")
print(" ")
print(perfil_social)
print(" ")
print(" ")

# 6 - Concatenando dados

with open("rede_INFNET.txt", "w") as arquivo:
    for linha in perfil_social:
        arquivo.write(str(linha) + "\n")

# 7 - Adicionando Amigos ⭐


def adicionar_amigo(nome_usuario, novo_amigo):
    for perfil in perfil_social:
        if perfil['nome'] == nome_usuario:
            perfil['amigos'].add(novo_amigo)
            print(f"{novo_amigo} foi adicionado à lista de amigos de {
                  nome_usuario}.")
            return

    print(f"Usuário {nome_usuario} não encontrado.")


print(" ### Adicionando amigos ###")
print(" ")
print(" ")
adicionar_amigo('Gabriela', 'Juliana')
print(perfil_social)
print(" ")
print(" ")


def verificando_conexoes(nome_usuario):
    contagem_nome = 0

    for perfil in perfil_social:
        if nome_usuario in perfil['amigos']:
            contagem_nome += 1
    if contagem_nome > 4:
        print(f"{nome_usuario} é um(a) Usuário(a) popular ")
    else:
        print(f"{nome_usuario} não é popular (conexões: {contagem_nome})")


print(" ### Usuario popular ###")
print(" ")
print(" ")
verificando_conexoes("Aline")
print(" ")
print(" ")


# 9 - Amigos em comum ⭐⭐

def amigos_em_comum():

    nomes_aleatorios = random.sample(perfil_social, 2)

    amigos_usuario_1 = nomes_aleatorios[0]['amigos']
    amigos_usuario_2 = nomes_aleatorios[1]['amigos']

    print(f"Usuário 1: {nomes_aleatorios[0]
          ['nome']} (Amigos: {amigos_usuario_1})")
    print(f"Usuário 2: {nomes_aleatorios[1]
          ['nome']} (Amigos: {amigos_usuario_2})")

    amigos_comuns = amigos_usuario_1.intersection(amigos_usuario_2)

    return amigos_comuns


print(" ### Amigos em comum ###")
print(" ")
print(" ")
amigos_comuns = amigos_em_comum()
print("Amigos em comum:", amigos_comuns)
print(" ")
print(" ")

# 10 -  Conexões Exclusivas ⭐⭐


def amigos_exclusivos():

    nomes_aleatorios = random.sample(perfil_social, 2)

    amigos_usuario_1 = nomes_aleatorios[0]['amigos']
    amigos_usuario_2 = nomes_aleatorios[1]['amigos']

    print(f"Usuário 1: {nomes_aleatorios[0]
          ['nome']} (Amigos: {amigos_usuario_1})")
    print(f"Usuário 2: {nomes_aleatorios[1]
          ['nome']} (Amigos: {amigos_usuario_2})")

    amigos_solo = amigos_usuario_1.difference(amigos_usuario_2)

    return amigos_solo


print(" ### Amigos exclusivos ###")
print(" ")
print(" ")
amigos_solo = amigos_exclusivos()
print("Amigos exclusivos:", amigos_solo)
print(" ")
print(" ")


# 11 - Removendo Conexões ⭐⭐
def removendo_amigos(usuario, remover_amigo):
    for perfil in perfil_social:
        if perfil["nome"] == usuario:
            perfil["amigos"].remove(remover_amigo)
            print(f"{removendo_amigos} foi removido da lista de amigos de {
                  usuario}.")
            return


print(" ### Removendo amigos ###")
print(" ")
print(" ")
removendo_amigos('Leonardo', 'Caio')
print(perfil_social)
print(" ")
print(" ")

# 12 - Salvando o Progresso ⭐⭐

with open("rede_INFNET_atualizado.txt", "w") as arquivo:
    for linha in perfil_social:
        arquivo.write(str(linha) + "\n")

# 13 - Listando Usuários ⭐

with open("rede_INFNET.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        separador = linha.strip().split(",")

        nome = separador[0]
        print(nome)

# 16 -  Lidando com arquivos ⭐⭐

# O recurso with torna o código legivel e claro ao programador, facilita o manuseio de arquivos com seus modos de leitura e escrita, fechamento automatico. Eu curti bastante o uso dele.


# enviado
