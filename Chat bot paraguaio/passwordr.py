def register(senha):
    arquivo = "senha.txt"

    with open(arquivo, "w", encoding='utf-8') as f:
        f.write(f"{senha}")