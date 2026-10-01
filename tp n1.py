#Definimos variables globales para poder mostrar los datos en el resumen
importePromedio = 0
importeDeLaVentaMasAlta = 0
cantidadTotalDeVentas = 0 
totalRecaudado = 0
sexoooo
cantidadTotalDeVentasEfectivo = 0
cantidadTotalDeVentasDebito = 0
cantidadTotalDeVentasCredito = 0

totalGolosinas = 0
totalBebidas = 0
totalAlmacen = 0
totalLibreria = 0

def calcularDescuentoPorMonto(subtotal):
    #esta funcion calcula el descuento por monto
    #recibe el subtotal y devuelve el monto con el descuento aplicado
  
    if (subtotal) > 25000:
      return subtotal * 0.9
    return subtotal

def CalcularAjustePorMedioDePago(monto, medioDePago):
    # Esta función calcula el ajuste según el medio de pago.
    # Recibe el monto y el medio de pago.
    # Devuelve el monto ajustado.
     if medioDePago == 1:
        return monto * 0.95
     elif medioDePago == 2:
         return monto
     elif medioDePago == 3:
         return monto * 1.08

def CalcularImporteFinal(subtotal, medioDePago):
    # Esta función calcula el importe final de una venta.
    # Recibe el subtotal y el medio de pago.
    # Devuelve el importe final.
    montoConDescuento = calcularDescuentoPorMonto(subtotal)
    importeFinal = CalcularAjustePorMedioDePago(montoConDescuento, medioDePago)
    return importeFinal

def verResumen():
    if cantidadTotalDeVentas == 0:
        return "Todavia no se registraron ventas."
    
    if cantidadTotalDeVentasEfectivo > cantidadTotalDeVentasDebito and cantidadTotalDeVentasEfectivo > cantidadTotalDeVentasCredito:
        medioMasUtilizado = "Efectivo"
    elif cantidadTotalDeVentasDebito > cantidadTotalDeVentasEfectivo and cantidadTotalDeVentasDebito > cantidadTotalDeVentasCredito:
        medioMasUtilizado = "Debito"
    else:
        medioMasUtilizado = "Credito"

    return f"""
        RESUMEN:
        Total recaudado: {totalRecaudado}
        Cantidad total de ventas: {cantidadTotalDeVentas}
        Recaudado por categoria:
        Golosinas: {totalGolosinas}
        Bebidas: {totalBebidas}
        Almacen: {totalAlmacen}
        Libreria: {totalLibreria}
        Importe venta más alta: {importeDeLaVentaMasAlta}
        Importe promedio: {importePromedio}

        Cantidad total de ventas efectivo: {cantidadTotalDeVentasEfectivo}
        Cantidad total de ventas debito: {cantidadTotalDeVentasDebito}
        Cantidad total de ventas credito: {cantidadTotalDeVentasCredito}
        Medio de pago mas utilizado: {medioMasUtilizado}
    """

def registrarVenta():
    categoria = solicitarNumeroEnRango("""Seleccione la categoria de su producto:
    1) Golosinas
    2) Bebidas
    3) Almacen
    4) Libreria
    """, 1, 4)

    precioUnitario = float(input("Escriba el precio unitario del producto: "))
    while precioUnitario <= 0:
        print("El precio debe ser mayor que cero.")
        precioUnitario = float(input("Escriba el precio unitario del producto: "))

    cantidad = solicitarNumeroEnRango("Escriba la cantidad de productos: ", 1, 999999)


    medioDePago = solicitarNumeroEnRango("""Seleccione el metodo de pago:
    1) Efectivo
    2) Debito
    3) Credito
    """, 1, 3)
    if categoria == 1:
        nombreCategoria = "Golosinas"
    elif categoria == 2:
        nombreCategoria = "Bebidas"
    elif categoria == 3:
        nombreCategoria = "Almacen"
    elif categoria == 4:
        nombreCategoria = "Libreria"

    subtotal = cantidad * precioUnitario
    montoConDescuento = calcularDescuentoPorMonto(subtotal)
    descuento = subtotal - montoConDescuento
    montoConAjuste = CalcularAjustePorMedioDePago(montoConDescuento, medioDePago)
    ajuste = montoConAjuste - montoConDescuento
    importeFinal = CalcularImporteFinal(subtotal, medioDePago)
    print(mostrarTicket(categoria, subtotal, descuento, ajuste, importeFinal))

    #modificamos variables globales para luego poder mostrar la informacion en el resumen
    global totalRecaudado
    global cantidadTotalDeVentas
    global importePromedio
    global importeDeLaVentaMasAlta

    totalRecaudado += importeFinal
    cantidadTotalDeVentas += 1
    importePromedio =  totalRecaudado / cantidadTotalDeVentas

    global cantidadTotalDeVentasEfectivo    
    global cantidadTotalDeVentasDebito
    global cantidadTotalDeVentasCredito

    if importeDeLaVentaMasAlta <= importeFinal:
        importeDeLaVentaMasAlta = importeFinal
    if medioDePago == 1:
        cantidadTotalDeVentasEfectivo += 1
    elif medioDePago == 2:  
        cantidadTotalDeVentasDebito += 1
    elif medioDePago == 3:
        cantidadTotalDeVentasCredito += 1


    global totalGolosinas
    global totalBebidas
    global totalAlmacen
    global totalLibreria

    if categoria == 1:
        totalGolosinas += importeFinal
    elif categoria == 2:
        totalBebidas += importeFinal
    elif categoria == 3:
        totalAlmacen += importeFinal
    elif categoria == 4:
        totalLibreria += importeFinal


def mostrarTicket(nombreCategoria, subtotal, descuento, ajuste, importeFinal):
    # Esta función muestra el ticket de una venta.
    # Recibe la categoria, el subtotal, el descuento, el ajuste y el importe final.
    # Devuelve un texto con el detalle de la venta.

    return f"""
    TICKET

    Categoria: {nombreCategoria}
    Subtotal: {subtotal}
    Descuento por monto: {descuento}
    Ajuste por medio de pago: {ajuste}
    Importe final: {importeFinal}
    """

def solicitarNumeroEnRango(mensaje, minimo, maximo):
    # Esta fue la funcion mas dificil de implementar ya que no encontrabamos un metodo
    # Para validar el tipo de dato de entrada, por lo que lo comparamos directamente con
    # los numeros en rango de str, si el string de entrada es 1,2,... puede
    # retornar el valor convertido en tipo entero
    # el caso recursivo es si el dato ingresado no es valido
    numero = input(mensaje)
    for i in range(minimo, maximo + 1):
        if numero == str(i):
            return int(numero)
        
    print("Numero invalido. Ingrese un valor dentro del rango.")
    return solicitarNumeroEnRango(mensaje, minimo, maximo)


def cuentaRegresiva(numero):
    # Esta función realiza la cuenta regresiva para cerrar la caja.
    # Recibe el numero desde el cual comienza la cuenta regresiva.
    # No devuelve un valor.
    if numero == 0:
        print("¡Caja cerrada!")
    else:
        print(numero)
        cuentaRegresiva(numero - 1)

def menuPrincipal():
    # Esta función muestra el menú principal y procesa la opción seleccionada.
    # Si el usuario cierra la caja, se solicita una confirmacion.
    # Nuestro caso base es si se confirma cerrar la caja
    # De lo contrario, se vuelve a llamar indefinidamente
    
    seleccion = solicitarNumeroEnRango("""Seleccione lo que quiera hacer:
    1) Registrar una venta
    2) Ver resumen
    3) Cerrar Caja
    """, 1, 3)

    if seleccion == 1:
        registrarVenta()
        menuPrincipal()
    elif seleccion == 2:
        print(verResumen())
        menuPrincipal()
    elif seleccion == 3:
        confirmacion = input("¿Esta seguro que desea cerrar la caja? (S/N): ")
        while confirmacion != "S" and confirmacion != "s" and confirmacion != "N" and confirmacion != "n":
            print("Respuesta invalida.")
            confirmacion = input("¿Esta seguro que desea cerrar la caja? (S/N): ")

        if confirmacion == "S" or confirmacion == "s":
           print(verResumen())
           cuentaRegresiva(5)
           return

        menuPrincipal()

        

menuPrincipal()
