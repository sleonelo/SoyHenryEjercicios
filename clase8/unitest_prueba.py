import unittest

def suma(num1,num2):
    return num1+num2

class caja_negra_test(unittest.TestCase):
    
    num1=10
    num2=20
    def test_de_la_suma_pos(self):
        resultado=suma(self.num1,self.num2)
        
        self.assertEquals(resultado, 30)
        self.assertTrue(self.num1+self.num2==30)
        
if __name__ == '__main__':
    unittest.main()