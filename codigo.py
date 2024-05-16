import os
import time
import sys


usuario={"admin":["123","adminstrador"],"user":["098","Vendedor"]}
cliente_nuevo=[]
clientes=[]
opcion_tienda=0
intentos_usuarios=3
inventario={"Codigo":["Nombre","Precio","Valor_initario","Descripcion"]}
cliente={"Documento":["Nombres","Apellidos","Correo","Telefono"]}



def menu_inicial():
    os.system("cls")
    print("""
    ╔════════════════════════════════════════════════════════════════╗  
    ║                                                                ║
    ║            BIENVENIDO AL SISTEMA DEl INVENTARIO                ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝ 

    """)
    validar_usuario(intentos_usuarios)

def menu_secundario():
    os.system("cls")
    print("""
    ╔════════════════════════════════════════════════════════════════╗  
    ║                       MENU DE INVENTARIO                       ║
    ╚════════════════════════════════════════════════════════════════╝ 
    
    [1]  Administracion del inventario
    [2]  Administracion de usuarios
    [3]  Administracion de clientes
    [4]  Generar ventas
    [0]  Salir
    """)

#Se esta generando el codigo para crear el menu de la administracion de clientes deL INVENTARIO
def menu_clientes():
    os.system("cls")
    print("""
    ╔════════════════════════════════════════════════════════════════╗  
    ║                        MENU  DE  INVENTARIO                    ║
    ╚════════════════════════════════════════════════════════════════╝ 

    [1] Ver los clientes
    [2] Agregar un cliente
    [3] Borrar un cliente
    [4] Actualizar dati de un cliente
    [5] Regresar al menu anterior
    [0] Salir
    
    """)  
    
    
#Se esta generando el codigo para crear el menu del inventario de la tienda   
def menu_inventario():
    os.system("cls")
    print("""
    ╔════════════════════════════════════════════════════════════════╗  
    ║                    INVENTARIO DE LA TIENDA                     ║
    ╚════════════════════════════════════════════════════════════════╝ 

    [1] Ver el inventario
    [2] Agregar producto al inventario
    [3] Borrar producto del inventario
    [4] Actualizar producto del inventario
    [5] Regresar al menu anterior
    [0] Salir
    
    """) 
    validar_inventario()
    
#Se esta generando el codigo para crear el menu del inventario de la tienda   
def menu_():
    os.system("cls")
    print("""
    ╔════════════════════════════════════════════════════════════════╗  
    ║                    INVENTARIO DE LA TIENDA                     ║
    ╚════════════════════════════════════════════════════════════════╝ 

    [1] Ver el inventario
    [2] Agregar producto al inventario
    [3] Borrar producto del inventario
    [4] Actualizar producto del inventario
    [5] Regresar al menu anterior
    [0] Salir
    
    """)  

    
def funcion_cliente():
    opcion_clientes =int(input("Digite el numero seleccionado:  "))  
    if opcion_tienda==1:
        os.system("cls")
        ver_cliente()
    elif opcion_clientes==2:
        agregar_cliente()
    elif opcion_clientes ==3:
        borrar_cliente()
    elif opcion_clientes ==4:
        actualizar_cliente()
    elif opcion_clientes ==5:
        pass

def validar_inventario():
    while True:
        opcion_inventario=int(input("Digite el numero seleccionado:  ")) 
        if opcion_inventario==1:
            ver_inventario()
            os.system("pause")
            os.system("cls")
            menu_inventario()
        elif opcion_inventario==2:
            agregar_inventario()
            os.system("pause")
            os.system("cls")
            menu_inventario()
        elif opcion_inventario==3:
            borra_inventario()
            os.system("pause")
            os.system("cls")
            menu_inventario()
        elif opcion_inventario==4:
            actuliza_inventario()
            os.system("pause")
            os.system("cls")
            menu_inventario()
        elif opcion_inventario==5:
            os.system("pause")
            os.system("cls")
            menu_secundario()
        elif opcion_inventario==0:
            print("Saliendo del sistema")
            os.system("pause")
            os.system("cls")
            salir_tienda()

def agregar_inventario():
    #inventario={"Codigo":["Elemento","Cantidad","Valor_initario","Descripcion"]}
    cod_producto=input("Digite el codigo del producto:  ")
    producto=input("Digite el nombre del producto:  ")
    valor_producto=input("Digite el valor unitario del producto:  ")
    cantidad_producto=input("Digite la cantidad de productos:  ")
    desc_prodcuto=input("Digite la descripcion del producto:  ")
    inventario[cod_producto]=[cod_producto,producto,valor_producto,cantidad_producto,desc_prodcuto]
    print("""
            ╔════════════════════════════════════════════════════════════════╗  
            ║              PRODUCTO AGREGADO AL INVENTARIO                   ║
            ╚════════════════════════════════════════════════════════════════╝ 
        """)
    os.system("pause")
    os.system("cls")
    
def borra_inventario():
    producto_borrar=input("Digite el codigo del producto:  ")
    if producto_borrar in inventario:
        inventario.pop(producto_borrar)
        print("""
            ╔════════════════════════════════════════════════════════════════╗  
            ║              PRODUCTO BORRADO DEL INVENTARIO                   ║
            ╚════════════════════════════════════════════════════════════════╝ 
        """)
    else:
        print("Producto no encontrado")

def actuliza_inventario():
    producto_actualizar=input("Digite el codigo del producto a actualizar:  ")
    print("""
          
          """)
    if producto_actualizar in inventario:
        print("""¿Que dato desea cambiar del producto:  
              [1] Cambiar el nombre del producto
              [2] Cambiar el valor del producto
              [3] Cambiar la cantidad del producto
              [4] Cambiar la descripcion del producto
              [0] Regresar a la pantalla anterior
              
              """)
        dato_producto_actualizar=int(input("Digite la opcion seleccionada:  "))
        if dato_producto_actualizar==1:
            val_actualizar=input("Digite el nombre del producto que va actualizar:  ")
        elif dato_producto_actualizar==2:
            val_actualizar=input("Digite el valor unitario del producto:  ")
        elif dato_producto_actualizar==3:
            val_actualizar=input("Digite la cantidad de productos:  ")
        elif dato_producto_actualizar==4:
            val_actualizar=input("Digite la descripcion del producto:  ")
        elif dato_producto_actualizar==0:
             validar_inventario()

        inventario[producto_actualizar][dato_producto_actualizar]=val_actualizar
        print("""
            ╔════════════════════════════════════════════════════════════════╗  
            ║             PRODUCTO ACTUALIZADO DEL INVENTARIO                ║
            ╚════════════════════════════════════════════════════════════════╝ 
        """)
    else:
        print("Producto no encontrado")

def ver_inventario():
    # Imprimir encabezados
    encabezados = inventario["Codigo"]
    print("")
    print("|  Codigo         "+"| {:<15} | {:<11} | {:<12} | {:<16} |".format(*encabezados))
    print("|" + "-"*17 + "|" + "-"*17 + "|" + "-"*12 + "|" + "-"*18 + "|"+ "-"*22 + "|")

    # Imprimir datos
    for codigo, datos in inventario.items():
        if codigo != "Codigo":  # Evitar imprimir nuevamente los encabezados
            print("| {:<15} | {:<15} | {:<10} | {:<16} | {:<20} |".format(*datos))

          
    
#SE DEFINE FUNCION PARA VALIDAR EL USUARIO Y LA CONTRASEÑA, SE PASAN PARAMETRO DE # DE INTENTOS
def validar_usuario(intentos_usuarios):
    while intentos_usuarios > 0 and intentos_usuarios <4:
        usrs=input("Ingrese su usuario: ")
        usrs=usrs.lower()  
        passwd=input("Digite su contraseña:  ")
        if usrs in usuario and usuario[usrs][0]==passwd:
            # Se debe tener en cuenta que tambien se puede acceder al espacio del tipo de usuario y dar
            # permisos de usuario y administrador. -- DEBEN CREAR EL ESPACIO PARA VALIDARLO SU ROL
            # EL ROL ADMINISTRADOR DEBE DAR PERMISOS DE:
            # -- ADMINISTRAR EL INVENTERIO
            # -- ADMINISTRAR LOS USUARIOS
            # EL ROL DE VENDEDOR DEBE DAR PERMISOS PARA:
            # -- ADMINISTRAR LOS CLIENTES
            # -- ADMINISTRAR LAS VENTAS
            menu_secundario()
            opcion_tienda=int(input("Digite el numero de la opcion seleccionada:  "))             
            if opcion_tienda==1:
                menu_inventario()
            elif opcion_tienda==2:
                pass
            elif opcion_tienda==3:
                agregar_cliente()
                menu_clientes()
            elif opcion_tienda==4:
                print("Estoy generando una venta")
            elif opcion_tienda==0:
                print("Saliendo del sistema")
                os.system("pause")
                os.system("cls")
                salir_tienda()
        else:
            os.system("cls")
            intentos_usuarios-=1
            print(f"""Ha digitado mal el usuario o la contraseña
                  
                  
                  .:: RECUERDE QUE LE QUEDAN {intentos_usuarios} OPORTUNIDADES MAS ::.
                  
                  """)
            os.system("pause")
            os.system("cls")
            
            
           

def agregar_cliente():
    documento_cliente=input("Digite el numero de documento: ")
    telefono_cliente=input("Digite le numero de telefo del cliente:  ")
    clientes.extend([documento_cliente,telefono_cliente])
    print(clientes)

def borrar_cliente():
    print("Borrando cliente")
    pass  

def ver_cliente():
    print("Visualizando todos los clientes")
    
def actualizar_cliente():
    print("Actualizando informacion del cliente")
    
def salir_tienda():
    sys.exit()

menu_inicial()