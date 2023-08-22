def search(pergunta):
    arquivo = "bot.txt"
    respostas = {}
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                perg = linha.strip().split("=")[0]
                resp = linha.strip().split("=")[1]
                respostas[perg.lower()] = resp.lower()
    except FileNotFoundError:
        return "Arquivo de treino não existe"
    return respostas.get(pergunta.lower(), "Não entendi sua questão")