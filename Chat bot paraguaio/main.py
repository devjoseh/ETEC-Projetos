import escreva as treina
import leia as ler
import hwriter as historico
import criptografia

questao = input("Treinar ou conversar: ")

if(questao.lower() == "treinar"):
    sair = "n"
    while sair.lower() != "sair":       
        pergunta = str(input("Digite uma pergunta: "))
        resposta = str(input("Digite uma resposta: "))

        pergunta = criptografia.encripta(pergunta)
        resposta = criptografia.encripta(resposta)
        treina.question(pergunta, resposta)
        sair = str(input("Enter para continuar, ou sair: "))
        if(sair.lower() == "sair"):
            break
elif (questao.lower() == "conversar"):
        sair = "n"
        while sair.lower() != "sair":       
            pergunta = str(input("Faça uma pergunta: "))
            sair = str(input("Enter para continuar, ou sair: "))
            if(sair.lower() == "sair"):
                break
            else:
                resultado = ler.search(pergunta)
                
                if(resultado == "Não entendi sua questão"):
                    print(resultado)
                    historico.history(pergunta)
                elif resultado == "Arquivo de treino não existe":
                    break
                else:
                    print(resultado)
else:
    exit