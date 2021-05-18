def asteriscos(str):
    cant = 0
    for i in range(len(str)):
        if (str[i])=='*':
            cant +=1
    return cant

texto1 = "h*o*l*a"
print (texto1 , "\t-> tiene  ", asteriscos(texto1), "*")
texto2 = "hola"
print (texto2 , "\t\t-> tiene  ", asteriscos(texto2), "*")

    
    
    
