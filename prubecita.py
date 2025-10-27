# Hola mundo 

def frase1(frase:str) -> float:
    precio = 0
    for i in frase:
        if i == "a""e""i""o""u":
            precio += 1
        elif i == " ":
            precio += 2
        else:
            precio += 0.5
    return precio
print (frase1("Hola Mundo")) # jdkfj
print (frase1("a a")) #4
#Hola


