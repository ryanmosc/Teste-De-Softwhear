import unittest

from teste3 import eh_par

class TesteValidaPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))
        
    def test_impar(self):
        self.assertFalse(eh_par(1))
    
if __name__=='__main__':
    unittest.main()
    