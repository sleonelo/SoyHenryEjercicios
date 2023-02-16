def primo1(num):
    num_prueba=2
    if num==1 or num==2:
        return True
    else:
        while (num) != (num_prueba):
            # print(num_prueba)
            # print(num)
            if num%num_prueba==0:
                num_prueba+=1
                return False
            else: num_prueba+=1 
        return True
        
#print(primo1(9))

def conversora(valor,origen,destino):
    if origen=='c' and destino=='f':
        return (valor*9/5)+32 
    if origen=='c' and destino=='k':
        return valor+273.15 
    if origen=='f' and destino=='c':
        return (valor-32)*(5/9)
    if origen=='f' and destino=='k':
        return (valor-32)*(5/9)+273.15
    if origen=='k'and destino=='c':
        return valor-273.15
    if origen=='k'and destino=='f':            
        return 1.8*(valor-273.15)+32        
    
#print(conversora(10,'k','f'), 'grados')

def factorial(num):
    inicial=1
    i=2
    while i<=num:
        inicial*=i
        i+=1
    return inicial

#print(factorial(5)) 