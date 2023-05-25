
opc=0

CP=250000
ID=475000
OB=800000

contCP=0
contID=0
contOB=0

subCP=0
subID=0
subOB=0
subtotal=0
total=0

while opc!=3:
   
    opc2=0
    print("-----------Binvenido a “El Diente de Oro”-----------")
    print("\n1) Realizar cotización")
    print("2) Renunciar (Generar otra cotizacion)")
    print("3) Salir")
    print("-"*35)

    while True:
        try:
            opc=int(input("\nEliga la opción correspondiente:\n"))
            if 1<= opc <=3:
                break
            else:
                print("La opcion está fuera de rango")
        except:
            print("Porfavor introduzca un numero entero entre 1 y 3")
    
    if opc==1:
        while opc2!=4:
            print("-"*35)
            print("Los tratamientos disponibles son los siguintes:")
            print("\n1) Carillas Porcelana      $250.000")
            print("2) Implantes Dentales      $475.000")
            print("3) Ortodoncia Brackets     $800.000")
            print("4) Salir")
            print("""\n# Todos los tratamientos incluyen:
            1- Limpieza y destartaje.
            2- Aplicacion de sellante.
            3- Aplicacion de fluor.""")
            while True:
                try:
                    opc2=int(input("\nEliga la opción correspondiente:\n"))
                    if 1<= opc <=4:
                        break
                    else:
                        print("La opcion está fuera de rango")
                except:
                    print("Porfavor introduzca un numero entero entre 1 y 3")
            
            if opc2==1:
                while True:
                    try:
                        cant=int(input("Correspondiente a este tratamiento ¿Cuantos desea cotizar? (Si preiono mal ingrese 0)\n"))
                        if cant>=0:
                            subCP+=CP*cant
                            subtotal+=CP*cant
                            contCP+=cant
                            break
                        else:
                            print("Numero invalido")
                    except:
                        print("Porfavor ingrese un numero entero mayor o igual a 0")

            if opc2==2:
                while True:
                    try:
                        cant=int(input("Correspondiente a este tratamiento ¿Cuantos desea cotizar? (Si preiono mal ingrese 0)\n"))
                        if cant>=0:
                            subID+=ID*cant
                            subtotal+=ID*cant
                            contID+=cant
                            break
                        else:
                            print("Numero invalido")
                    except:
                        print("Porfavor ingrese un numero entero mayor o igual a 0")

            if opc2==3:
                while True:
                    try:
                        cant=int(input("Correspondiente a este tratamiento ¿Cuantos desea cotizar? (Si preiono mal ingrese 0)\n"))
                        if cant>=0:
                            subOB+=OB*cant
                            subtotal+=OB*cant
                            contOB+=cant
                            break
                        else:
                            print("Numero invalido")
                    except:
                        print("Porfavor ingrese un numero entero mayor o igual a 0")

            if opc2==4:
                while True:
                    try:
                        print("Para calcular esta cotizacion es necesario que ingrese que cargo ocupa usted:")
                        print("1) Trabajador Auxiliar, se aplicará un descuesto del 15%")
                        print("2) Trabajador Administrativo, se aplica un descuento del 10%")
                        print("3) Trabajador Docente, 5% descuento")
                        trab=int(input("\nIngrese la opción que corresponda a su cargo:\n"))
                        if 1<= trab <=3:
                            break
                        else:
                            print("Numero fuera de rango")
                    except:
                        print("Ingrese un numero entero entre 1 y 3")

                if trab==1:
                    total=subtotal-((subtotal*15)/100)
                    print("-"*50)
                    print("                      Cotización")
                    print("-"*50)
                    print(f"--> {contCP} tratamiento(s) Carillas Porcelana      ${subCP}")
                    print(f"--> {contID} tratamiento(s) Implantes Dentales      ${subID}")
                    print(f"--> {contOB} tratamiento(s) Ortodoncia Brackets     ${subOB}")
                    print("-"*50)
                    print(f"Subtotal:    ${subtotal}")
                    print("Descuento:    15%")
                    print("-"*50)
                    print(f"Total        ${total}")
                    print("-"*50)
                    print(f"Son 12 cuotas de: ${round(total/12)}")
                    print("\nSonria Bonito")

                if trab==2:
                    total=subtotal-((subtotal*10)/100)
                    print("-"*50)
                    print("                      Cotización")
                    print("-"*50)
                    print(f"--> {contCP} tratamiento(s) Carillas Porcelana      ${subCP}")
                    print(f"--> {contID} tratamiento(s) Implantes Dentales      ${subID}")
                    print(f"--> {contOB} tratamiento(s) Ortodoncia Brackets     ${subOB}")
                    print("-"*50)
                    print(f"Subtotal:    ${subtotal}")
                    print("Descuento:    10%")
                    print("-"*50)
                    print(f"Total        ${total}")
                    print("-"*50)
                    print(f"Son 12 cuotas de: ${round(total/12)}")
                    print("\nSonria Bonito")

                if trab==3:
                    total=subtotal-((subtotal*5)/100)
                    print("-"*50)
                    print("                      Cotización")
                    print("-"*50)
                    print(f"--> {contCP} tratamiento(s) Carillas Porcelana      ${subCP}")
                    print(f"--> {contID} tratamiento(s) Implantes Dentales      ${subID}")
                    print(f"--> {contOB} tratamiento(s) Ortodoncia Brackets     ${subOB}")
                    print("-"*50)
                    print(f"Subtotal:    ${subtotal}")
                    print("Descuento:    5%")
                    print("-"*50)
                    print(f"Total        ${total}")
                    print("-"*50)
                    print(f"Son 12 cuotas de: ${round(total/12)}")
                    print("\nSonria Bonito")

    if opc==2:
        contCP=0
        contID=0
        contOB=0
        subCP=0
        subID=0
        subOB=0
        subtotal=0
        total=0
        print("Realizando otra cotizacion...")
    
    if opc==3:
        print("¡Hasta pronto!")