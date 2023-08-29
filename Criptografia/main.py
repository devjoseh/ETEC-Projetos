alfabeto = "abcdefghijklmnopqrstuvwxyz1234567890 "
cripto = "bcdefghijklmnopqrstuvwxyza2345678901/"

criptografar = {alfabeto[i]: cripto[i] for i in range(len(alfabeto))}
descripto = {cripto[i]: alfabeto[i] for i in range(len(cripto))}

def encripta(texto):
    texto_cripto = ""
    for char in texto:
        texto_cripto += criptografar.get(char, char)
    return texto_cripto

def descripta(texto):
    texto_descripto = ""
    for char in texto:
        texto_descripto += descripto.get(char, char)
    return texto_descripto

print(encripta("piada"))