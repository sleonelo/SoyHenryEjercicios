import unittest

def suma(num1,num2):
    return num1+num2

class caja_negra_test(unittest.TestCasepython):
    
    def test_de_la_suma_pos(self):
        num1=10
        num2=20
        resultado=suma(num1,num2)
        
        self.assertEquals(resultado, 30)