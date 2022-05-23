from Coche import Coche
escuderias=list()
 
opcion=0
while(opcion!=5):
    print("__________________________________")
    print("              Menú                ")
    print("__________________________________")
    print("1--> Registrar escuderia. ")
    print("2--> Mostrar escuderia mas cara. ")
    print("3--> Mostrar cuantas tienen mercedes, ferrari y cuantas renault")
    print("4--> Buscar y eliminar producto. ")
    print("5--> SALIR ")
    print("__________________________________")
 
    opcion=int(input("Digite la opción deseada: "))
    print("__________________________________")
    ocoche=Coche()
    if(opcion==1):
        try:
            print("ESCUDERIA")
            ocoche.nombreEscu=input("Digite el nombre de la escuderia: ")
            ocoche.motor=input("Digite el motor: (Mercedes/Ferrari/Renault/Honda): ")
            ocoche.piloto=input("Digite el nombre del piloto: ")
            ocoche.costo=input("Digite el costo anual de la escuderia: ")
            escuderias.append(ocoche)
        except:
            print("No se guardo la escuderia")
    elif(opcion==2):
        mascara = sorted(escuderias,key = lambda escuderia: escuderia.costo)
        print(f"la escuderia mas cara es {mascara[0].nombreEscu} con el valor de: ${mascara[0].costo}")
 
    elif(opcion==3):
        for escuderia in escuderias:
            mercedes = len(list(filter(lambda escuderia:  escuderia.motor=="mercedes",escuderias)))
            ferrari = len(list(filter(lambda escuderia:  escuderia.motor=="ferrari",escuderias)))
            renault = len(list(filter(lambda escuderia: escuderia.motor=="renault",escuderias)))
            honda = len(list(filter(lambda escuderia: escuderia.motor=="honda",escuderias)))
           
        totalEscuderias={'mercedes':mercedes, 'ferrari':ferrari, 'renault': renault, 'honda': honda}
        print(f'El inventario esta distribuido de la siguiente manera: {totalEscuderias}')
    elif(opcion==5):
        print("Gracias por preferirnos")
 
    else:
        print("Ingrese una opcion valida")

