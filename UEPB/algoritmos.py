# -------------- Passo 1 e 2 --------------
#angulos = input("Digite os ângulos: ").split()
#angulos = "18g25m1s 21g 1g50s 49s 46g59m 40m17s".split()
angulos = "18g25m1s 21g 1g50s 49s 46g59m".split()

try:
    somaGraus = 0
    somaMinutos = 0
    somaSegundos = 0
    media = 0
    objeto = {}
    for i in range(len(angulos)):
        graus = 0
        minutos = 0
        segundos = 0

        if(angulos[i].__contains__("g")):
            graus = angulos[i].split("g")[0]
            somaGraus += int(graus)

        if(angulos[i].__contains__("m")):
            minutos = angulos[i].split("m")[0]
            if(minutos.__contains__("g")):
                minutos = minutos.split("g")[1]
            somaMinutos += int(minutos)
                
        if(angulos[i].__contains__("s")):
            segundos = angulos[i].split("s")[0]
            if(segundos.__contains__("m")):
                segundos = segundos.split("m")[1]
            if(segundos.__contains__("g")):
                segundos = segundos.split("g")[1]
            somaSegundos += int(segundos)

        coordenadas = (int(graus), int(minutos), int(segundos))
        objeto[angulos[i]] = coordenadas
except:
    print("O valor passado está com formato inválido")
    exit()   

print(objeto)

# -------------- Passo 3 --------------
segundos = somaSegundos % 60
somaMinutos += (somaSegundos - segundos)/60
minutos = int(somaMinutos % 60)
somaGraus += (somaMinutos - minutos)/60
graus = int(somaGraus)

print(f"A soma de todos os ângulos é de: {graus}g{minutos}m{segundos}s")

restoGraus = graus % len(angulos)
graus /= len(angulos)
restoMinutos = (minutos + (restoGraus * 60)) % len(angulos)
minutos = (minutos + (restoGraus * 60)) / len(angulos)
restoSegundos = (segundos + (restoMinutos * 60)) % len(angulos)
segundos = (segundos + (restoMinutos * 60)) / len(angulos)

print(f"A média de todos os ângulos é de: {int(graus)}g{int(minutos)}m{int(segundos)}s")