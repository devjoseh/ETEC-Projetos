def history(pergunta):
    arquivo = "historico.txt"

    with open(arquivo, "a", encoding='utf-8') as f:
        f.write(f"{pergunta}\n")