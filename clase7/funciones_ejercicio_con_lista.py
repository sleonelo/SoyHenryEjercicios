import funcionescreadas as fc

class Funciones_antiguas():
    def __init__(self,lista) -> None:
        self.lista=lista
    
    def primo(self):
        validacion=[fc.primo1(i) for i in self.lista]
        definitiva=zip(self.lista,validacion)
        return(list(definitiva))
        
        
    def conversora_c(self,origen, destino):
        resultados=[fc.conversora(i,origen,destino) for i in self.lista]
        definitiva=zip(self.lista,resultados)
        return(list(definitiva))
        
    def factorial_c(self):
        validacion_f=[fc.factorial(i) for i in self.lista]
        resultados=zip(self.lista,validacion_f)
        return(list(resultados))
        
# objeto_test_lista=Funciones_antiguas([2,4,6,7,11,13])
# objeto_test_lista.primo()
# objeto_test_lista.conversora_c('c','f')
# objeto_test_lista.factorial_c()