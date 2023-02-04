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


def percepciones(producto):
    per = (producto * 45) / 100
    return per

def ingresos_brutos(producto):
    i_b =(producto * 3)/100
    return i_b


def test():
    print("\033[1;30;46mBienvenido al sistema de calculo de precios de productos extranjeros con impuesto(iva,pais,extranjero).")
    producto = Mayor_que(0,"\033[1;33mIntroduzca el precio base del producto: ")
    iva = Iva(producto)
    i_p = Impuesto_Pais(producto)
    per = percepciones(producto)
    i_b = ingresos_brutos(producto)
    final = iva + i_p + per + producto + i_b
    print("\033[1;33mEl precio final es: ",round(final,2))
    input("Ingrese cualquier tecla para terminar: ")

if __name__ == "__main__":
    test()
