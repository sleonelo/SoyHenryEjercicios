import funcionescreadas

class Funciones_antiguas():
    def __init__(self) -> None:
        pass
    
    def primo(self,num):
        validacion=funcionescreadas.primo1(num)
        print(validacion)
        
    def conversora_c(self, valor, origen, destino):
        print(funcionescreadas.conversora(valor,origen,destino))
        
    def factorial_c(self, num):
        print(funcionescreadas.factorial(num))
    

# objeto_de_prueba=Funciones_antiguas()

# objeto_de_prueba.primo(7)

# objeto_de_prueba.conversora_c(10,'c','k')

# objeto_de_prueba.factorial_c(5)