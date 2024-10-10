def eh_par(numero):
    return numero %2==0

import unittest

class TesteValidaPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))
        
    def test_impar(self):
        self.assertFalse(eh_par(1))
    
if __name__=='__main__':
    unittest.main()
    