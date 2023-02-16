lista=list(range(1,11))
divisor=0.5
def dividir_elementos(lista,divisor):
    #for i in lista: devuelve el primer elemento de la lista y ahi se queda
    
    return [int(i/divisor) for i in lista] #en cambio de esta forma devuelve toda la lista
    
print(dividir_elementos(lista,divisor))