import criptografia
import password as senha
import archives

senha_ativa = False

questao = input("Treinar ou conversar: ")

if(questao.lower() == "treinar"):
    sair = "n"
    while sair.lower() != "sair": 
        
        if(senha_ativa == False):
            senha_digitada = senha.treinar()
            if(senha_digitada == "Inexistente"):
                print("Não existe nenhuma senha configurada")
                break
            if(senha_digitada == False):
                print("Senha incorreta, acesso negado.")
            else:
                senha_ativa = True

        while(senha_ativa == True):
            pergunta = str(input("Digite uma pergunta: "))
            resposta = str(input("Digite uma resposta: "))
            pergunta = criptografia.encripta(pergunta)
            resposta = criptografia.encripta(resposta)
            archives.write(pergunta, resposta)
            sair = str(input("Enter para continuar, ou sair: "))
            if(sair.lower() == "sair"):
                senha_ativa = False
                break
elif (questao.lower() == "conversar"):
        sair = "n"
        while sair.lower() != "sair":       
            pergunta = str(input("Faça uma pergunta: "))

            perguntaCrip = criptografia.encripta(pergunta)
            
            resultado = archives.search(perguntaCrip)
            
            if(resultado == "Não entendi sua questão"):
                print(resultado)
                archives.historic(perguntaCrip)
            elif resultado == "Arquivo de treino não existe":
                break
            else:
                print(resultado)
            
            sair = str(input("Enter para continuar, ou sair: "))
            if(sair.lower() == "sair"):
                break

elif (questao.lower() == "configurar"):
    senhaNova = str(input("Digite qual será a nova senha: "))
    archives.password(senhaNova)
    print("Senha nova registrada com sucesso!")
else:
    exit