#Faça um programa que retorne a pontuação de uma senha, podendo assim ser avaliada se é forte ou não. \
# Utilize a tabela de resultado abaixo para informar ao usuário se a senha escolhida é muito fraca, fraca, boa, forte ou muito forte.
# Pontuação < 20): "Muito fraca"
# 20 <= Pontuação < 40): "Fraca"
# 40 <= Pontuação < 60): "Boa"
# 60 <= Pontuação < 80): "Forte"
# 80 <= Pontuação: "Muito forte"
# --------------------
# fazer funcao para escrever a senha
# fazer funcao para avaliar a senha
import string

def criar_senha():
    while True:
        senha = input("Digite sua senha: ")
        print("Senha criada com sucesso!")
        return senha

def calcular_pontuacao(senha):
    pontuacao = 0
    total_carac = len(senha)
    maiuscula = sum(1 for c in senha if c.isupper())
    minuscula = sum(1 for c in senha if c.islower())
    numero = sum(1 for c in senha if c.isdigit())
    simbolos = sum(1 for c in senha if not c.isalnum())
    meio = sum(1 for c in senha[1:-1] if not c.isalnum())

    # Adições
    pontuacao += total_carac * 4
    pontuacao += (total_carac - maiuscula) * 2
    pontuacao += (total_carac - minuscula) * 2
    pontuacao += numero * 4
    pontuacao += simbolos * 6
    pontuacao += meio * 2

    # Regras extras
    totaL_regras = sum([maiuscula > 0, minuscula > 0, numero > 0, simbolos > 0, total_carac >= 8])
    pontuacao += (totaL_regras * 2)

    # Deduções
    if senha.isalpha():
        pontuacao -= total_carac
    elif senha.isdigit():
        pontuacao -= numero

    pontuacao -= contar_repetidos(senha)
    pontuacao -= contar_sequenciais(senha, 3) * 3
    pontuacao -= contar_repetidos_consecutivos(senha, str.isupper) * 2
    pontuacao -= contar_repetidos_consecutivos(senha, str.islower) * 2
    pontuacao -= contar_sequenciais(senha, 3, lambda c: not c.isalnum()) * 3
    pontuacao -= contar_repetidos_consecutivos(senha, str.isdigit) * 2

    return pontuacao

def contar_repetidos(senha):
    return sum(1 for i in range(len(senha) - 1) if senha[i].lower() == senha[i + 1].lower())

def contar_sequenciais(senha, n, cond=lambda c: c.isalpha()):
    return sum(1 for i in range(len(senha) - n + 1) if all(cond(senha[i + j]) and senha[i + j].lower() == senha[i].lower() for j in range(n)))

def contar_repetidos_consecutivos(senha, cond):
    return sum(1 for i in range(len(senha) - 1) if cond(senha[i]) and senha[i] == senha[i + 1])

def classificar_forca(pontuacao):
    if pontuacao < 20:
        return "Muito fraca"
    elif pontuacao < 40:
        return "Fraca"
    elif pontuacao < 60:
        return "Boa"
    elif pontuacao < 80:
        return "Forte"
    else:
        return "Muito forte"

senha = criar_senha()
pontuacao = calcular_pontuacao(senha)
forca = classificar_forca(pontuacao)
print(f"Sua senha: {senha}, Pontuação total: {pontuacao}, Força: {forca}")