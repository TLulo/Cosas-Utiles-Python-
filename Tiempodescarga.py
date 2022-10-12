def Bienvenida():
    print("Bienvenido al sistema para calcular la duracion de la descarga.")
    input("Presione Enter para continuar: ")
def Menu():
    print("*"*100)
    print("Su archivo a descargar se mide en: ")
    print("0- Cerrar"
          "\n1- Kb"
          "\n2- Mb"
          "\n3- Gb"
          "\n4- Tb")
    x = int(input("Ingrese una opcion valida: "))
    return x
def Sistema_menu():
    velocidad = Entrada()
    x = Menu()
    if x == 0:
        print("|","*"*18,"|")
        print("|Cerrando Sistema|")
        print("|","*"*18,"|")
    elif x > 0 and x < 5 :
        n = float(input("Introduzca el tamaño de la descarga: "))
        if x == 1:
            a = n / 1000
        elif x == 2:
            a = n
        elif x == 3:
            a = n * 1000
        elif x == 4:
            a = n * 1000000
        horas,min,seg = tiempo(a,velocidad)
        print("El tiempo que durara la descarga es: ",horas,":",min,":",seg)

        pass
def tiempo(x,i):
    a = x / i
    b = a % 3600
    horas = int(a // 3600)
    min = int(b / 60)
    seg = int(b % 60)
    return horas,min,seg

def Entrada():
    print("*"*100)
    velocidad = float(input("Introduzca su velocidad de descarga(MB/s): "))
    return velocidad

def test():
    Bienvenida()
    Sistema_menu()
    input("Presione Enter para finalizar: ")
if __name__ == "__main__":
    test()
