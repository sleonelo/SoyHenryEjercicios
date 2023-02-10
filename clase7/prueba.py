rango=list(range(1,21))
def pares(numeros):
    pares=[]
    for i in numeros:
        if i%2==0:
           pares.append(i)
    return pares 

#print(pares(rango)) 


def pares_iterados(numeros):
    for i in numeros:
        if i%2==0:
           yield i
    
test_yield=list(pares_iterados(rango))
#print(test_yield)
numero=5

def pares_optimizada(numero):
    inicio=1
    while inicio<numero:
        yield (inicio*2)
        inicio+=1
    

print(list(pares_optimizada(numero)))