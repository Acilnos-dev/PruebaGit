def frase1(frase:str) -> float:
    precio = 0
    for i in frase:
        if i == "a""e""i""o""u":
            precio += 1
        elif i == frase.lower:
            precio += 0.5
    return precio
print (frase1("Hola Mundo"))