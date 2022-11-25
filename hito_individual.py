#creo una clase Registro
class Registro:

    def __init__(self,nombre,apellido,edad,correo,telefono,direccion,pais,contraseña):  #constructor
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.correo=correo
        self.telefono=telefono
        self.direccion=direccion
        self.pais=pais
        self.contraseña=contraseña


    def inicioPrograma():  #creamos  funcion para que se registre o inicie sesion
        
        inicio=True   
        iniciosesion=input('Escriba I para iniciar sesion o R para registrarse \n').upper() 
        while inicio == True:  #bucle para que se tenga que registrar
            reg=False
            if iniciosesion == 'R':
                nombre=input('Escriba su nombre: \n').upper()
                apellido=input('Escriba su apellido: \n').upper()
                edad=input('Escriba su edad: \n').upper()
                correo=input('Escriba su correo electronico: \n').upper()
                telefono=input('Escriba su numero de telefono: \n').upper()
                direccion=input('Escriba su direcion: \n').upper()
                pais=input('Escriba su pais: \n').upper()
                contraseña=input('Escoja una contraseña \n').upper()
                
                usuario=[nombre,apellido,edad,correo,telefono,direccion,pais,contraseña]
                print(usuario)
                reg=True
                inicio=False
            elif iniciosesion == 'I'and reg == False:
               print('usuario no existe, Registrese')
               iniciosesion=input('Escriba R para registrarse \n').upper() 
            else:
                print('ingrese I o R')
                iniciosesion=input('Escriba I para iniciar sesion o R para registrarse \n').upper() 
    inicioPrograma() 
    print('\n Realize su pedido \n')
    
#creamos una clase que herede de Registro por si es necesario utilizar algun dato de esta clase
class Producto(Registro):

    
    def __init__(self,id,nombreProducto,descripcion,precio,cantidad): #constructor
        self.id=id
        self.nombreProducto=nombreProducto
        self.descripcion=descripcion
        self.precio=precio
        self.cantidad=cantidad
    
    #muestra los productos que se pueden comprar
    print('A','mesa','mesa redonda',20,1)
    print('B','silla','silla madera',8,4)
    print('C','pantalon','pantalon corto',12,1)
    print('D','calcetines','calcetines negros',7,6)

    #creamos una funcion que usaremos luego para que nos imprima el producto deseado
    def selecionProducto(self):
        print(f'Ha añadido a la cesta el producto {self.nombreProducto} cuyo identificador es "{self.id}" se trata de {self.descripcion}, tiene un coste de {self.precio} y se va a llevar {self.cantidad} unidades ')
A=Producto('A','mesa','mesa redonda',20,1)
B=Producto('B','silla','silla madera',8,4)
C=Producto('C','pantalon','pantalon corto',12,1)
D=Producto('D','calcetines','calcetines negros',7,6)

#utilizo un bucle para que pueda seguir comprando mas productos
continuar = True
while continuar:
    selecProducto=input('Selecione un producto de los recien mostrados mediante su identificador o pulse P para ir a pagar ')    
    if selecProducto =='a' or selecProducto == 'A':
            print(A.selecionProducto())
            continuar=input('¿Desea añadir mas prouctos?(si/no) ') == 'si' 
    elif selecProducto == 'b' or selecProducto == 'B':
            print(B.selecionProducto())
            continuar=input('¿Desea añadir mas prouctos?(si/no) ') == 'si' 
    elif selecProducto =='c' or selecProducto == 'C':
            print(C.selecionProducto()) 
            continuar=input('¿Desea añadir mas prouctos? ') == 'si' 
    elif selecProducto =='d' or selecProducto == 'D':
            print(D.selecionProducto()) 
            continuar=input('¿Desea añadir mas prouctos?(si/no) ') == 'si' 
    elif selecProducto == 'p' or selecProducto == 'P':
            print('solo admitimos pagos con tarjeta de debito o credito')
            gmail=input('introduzca su correo electronico: ')
            print(f'su gmail es {gmail}')
            try:
                telf=(int(input('Introduzca su número de telefono: ')))
            except:
                print('Has introducido un carácter que no es un número, introduzca un número para poder continuar')
                telf=(int(input('Introduzca su número de telefono: ')))
            print(f'se enviara la factura como pdf a {gmail}')
            print(f'no olvide revisar los mensajes del numero {telf} y el correo {gmail} donde le llegara un seguimiento de su pedido')
            print(f'Gracias pr su compra')
            continuar=input('¿Desea hacer una nueva compra?(si/no) ') == 'si' 
            
    else:
        print('digito no valido') 
        continuar=input('¿Desea añadir mas prouctos?(si/no) ') == 'si'
