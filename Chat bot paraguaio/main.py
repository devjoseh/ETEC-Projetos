import escreva as treina
import leia as ler
import hwriter as historico
import criptografia
import treinar as senha
import passwordr

senha_ativa = False

questao = input("Treinar ou conversar: ")

if(questao.lower() == "treinar"):
    sair = "n"
    while sair.lower() != "sair": 
        
        if(senha_ativa == False):
            senha_digitada = senha.treinar()
            if(senha_digitada == False):
                print("Senha incorreta, acesso negado.")
            else:
                senha_ativa = True

        while(senha_ativa == True):
            pergunta = str(input("Digite uma pergunta: "))
            resposta = str(input("Digite uma resposta: "))
            pergunta = criptografia.encripta(pergunta)
            resposta = criptografia.encripta(resposta)
            treina.question(pergunta, resposta)
            sair = str(input("Enter para continuar, ou sair: "))
            if(sair.lower() == "sair"):
                senha_ativa = False
                break
elif (questao.lower() == "conversar"):
        sair = "n"
        while sair.lower() != "sair":       
            pergunta = str(input("Faça uma pergunta: "))

            perguntaCrip = criptografia.encripta(pergunta)
            
            resultado = ler.search(perguntaCrip)
            
            if(resultado == "Não entendi sua questão"):
                print(resultado)
                historico.history(perguntaCrip)
            elif resultado == "Arquivo de treino não existe":
                break
            else:
                print(resultado)
            
            sair = str(input("Enter para continuar, ou sair: "))
            if(sair.lower() == "sair"):
                break

elif (questao.lower() == "configurar"):
    senhaNova = str(input("Digite qual será a nova senha: "))
    passwordr.register(senhaNova)
    print("Senha nova registrada com sucesso!")
else:
    exit