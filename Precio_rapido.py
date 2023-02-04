
def Mayor_que(men,texto):
    k = -1
    while k < men:
        k = float(input(texto))
    return k


def Iva(producto):
    iva = (producto * 21) / 100
    return iva


def Impuesto_Pais(producto):
    i_p = (producto * 8)/100
    return i_p


def Impuesto_Extranjero(producto):
    i_ex = (producto * 35) / 100
    return i_ex


def test():
    print("\033[1;30;46mBienvenido al sistema de calculo de precios de productos extranjeros con impuesto(iva,pais,extranjero).")
    producto = Mayor_que(0,"\033[1;33mIntroduzca el precio base del producto: ")
    iva = Iva(producto)
    i_p = Impuesto_Pais(producto)
    i_ex = Impuesto_Extranjero(producto)
    final = iva + i_p + i_ex + producto
    print("\033[1;33mEl precio final es: ",final)
    input("Ingrese cualquier tecla para terminar: ")

if __name__ == "__main__":
    test()
