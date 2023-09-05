senha = "1234"

def treinar():
    pedir_senha = str(input("Digite a senha de acesso: "))

    if(pedir_senha != senha):
        return False
    else:
        return True

