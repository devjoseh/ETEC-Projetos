import escreva as treina
import leia as ler

questao = input("Treinar ou conversar: ")

if(questao.lower() == "treinar"):
    sair = "n"
    while sair.lower() != "sair":       
        pergunta = str(input("Digite uma pergunta: "))
        resposta = str(input("Digite uma resposta: "))
        treina.question(pergunta, resposta)
        sair = str(input("Enter para continuar, ou sair: "))
elif (questao.lower() == "conversar"):
        sair = "n"
        while sair.lower() != "sair":       
            pergunta = str(input("Faça uma pergunta: "))
            print(ler.search(pergunta))
            sair = str(input("Enter para continuar, ou sair: "))
