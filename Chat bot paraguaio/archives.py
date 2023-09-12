import criptografia

# Escrever as perguntas e respostas no arquivo bot.txt
def write(pergunta, resposta):
    arquivo = "dados/bot.txt"
    with open(arquivo, "a", encoding='utf-8') as f:
        f.write(f"{pergunta}={resposta}\n")

# Faz a pesquisa das perguntas e acha a resposta dentro do arquivo bot.txt
def search(pergunta):
    arquivo = "dados/bot.txt"
    respostas = {}
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                perg = linha.strip().split("=")[0]
                resp = linha.strip().split("=")[1]
                respostas[perg.lower()] = criptografia.descripta(resp.lower())
    except FileNotFoundError:
        return "Arquivo de treino não existe"
    return respostas.get(pergunta.lower(), "Não entendi sua questão")

# Quando o usuário fizer uma pergunta, ela é registrada no histórico caso não seja encontrada
def historic(pergunta):
    arquivo = "dados/historico.txt"

    with open(arquivo, "a", encoding='utf-8') as f:
        f.write(f"{pergunta}\n")

# Registra uma nova senha
def password(senha):
    arquivo = "dados/senha.txt"

    with open(arquivo, "w", encoding='utf-8') as f:
        f.write(f"{criptografia.encripta(senha)}")
