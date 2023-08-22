def question(pergunta, resposta):
    arquivo = "bot.txt"

    with open(arquivo, "a", encoding='utf-8') as f:
        f.write(f"{pergunta}={resposta}\n")