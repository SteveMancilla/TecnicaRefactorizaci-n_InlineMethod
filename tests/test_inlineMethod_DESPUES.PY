import unittest
from inlineMethod_ANTES import Numeros

class NumerosParesImpares(unittest.TestCase):
    
    def setUp(self):
        self.dividir = Numeros()
    
    def tearDown(self):
        self.dividir = None
    
    def test_NumeroParImpar(self):
        
        numeros=[1,2,3,4,5,6,7]
        resultado_esperado_pares = [2,4,6]
        resultado_esperado_impares = [1,3,5,7]
        
        resultado_actual_pares, resultado_actual_impares = self.dividir.separar_numeros(numeros)
        
        self.assertEqual(resultado_esperado_pares, resultado_actual_pares)
        self.assertEqual(resultado_esperado_impares, resultado_actual_impares)

if __name__=='__main__':
    unittest.main()