
def inicio(): 
    print("-----------bienvenido al programa--------------")

def suma(): 

   
    
    while  numeros != "n":
      materia1 = int(input("ingrese el promedio de la meria 1: "))
      materia2 = int (input("ingrese la materia 2: "))
      materia3 = int(input("ingrese la materia 3: "))
      sumapromedio =  materia1 + materia2 + materia3
      numeros = input("¿Deseas continuar s=si & n=no: ")
    return numeros

    promedio(sumapromedio)
  

def promedio(sumapromedio):
    
    promedio1 = sumapromedio/3
    print(f"el promedio es: {promedio1}")

    if(promedio1 > 6): {
      print("el alumno pasa")
    }
    else:
        {print("no pasa")}

def menss(mensaje): 
    print(f"el mensaje es: {mensaje}")

def salida():
    print("----------has salido del programa---------------")

mensaje = input("da un mensaje al maestro: ")

inicio()
suma()
menss(mensaje)
salida()



    





