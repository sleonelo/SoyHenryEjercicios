lista=list(range(1,11))
divisor=0.5
def dividir_elementos(lista,divisor):
    #for i in lista: devuelve el primer elemento de la lista y ahi se queda
    
    return [int(i/divisor) for i in lista] #en cambio de esta forma devuelve toda la lista
    
#print(dividir_elementos(lista,divisor))

import sys
sys.path.append('/home/silvio/Escritorio/SoyHenryEjercicios/clase7')

# import clase7
# dir (clase7)
# import sys
#print(sys.path)
import funcionescreadas as fc
import funciones_ejercicio_con_lista as fel

# objeto_importado=fel.Funciones_antiguas([1,2])
# print(objeto_importado.primo())

