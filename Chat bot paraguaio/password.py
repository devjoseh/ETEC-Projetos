def ler():
    with open("dados/senha.txt", "r", encoding="utf-8") as f:
        for linha in f:
            senhaR = linha
            return senhaR

senha = ler()

def treinar():
    pedir_senha = str(input("Digite a senha de acesso: "))

    if(pedir_senha != senha):
        return False
    else:
        return True
