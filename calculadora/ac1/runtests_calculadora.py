import unittest
import requests

class TestStringMethods(unittest.TestCase):



     def test_00_soma(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"soma"})
         if "30" not in r1.text:
             self.fail("a soma de 10 com 20 deveria ter dado trinta")

     def test_01_divisao(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"div"})
         if "0.5" not in r1.text:
             self.fail("10/20 deveria ter dado 0.5")

     def test_02_mult(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"mult"})
         if "20" not in r1.text:
             self.fail("o produto de 10 com 20 deveria ter dado 200")

     def test_03_sub(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':30,"b":20, "ope":"sub"})
         if "10" not in r1.text:
             self.fail("subtrair 20 de 30 deveria ter dado 10")

     def test_04_divisao_por_zero(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":0, "ope":"div"})
         if "ERRO" not in r1.text:
             self.fail("10/0 deveria ter dado um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")

     def test_05_a_inteiro(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':'banana',"b":20, "ope":"soma"})
         if "ERRO" not in r1.text:
             self.fail("Enviei um a inválido, esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     def test_05_b_inteiro(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'b':'banana',"a":20, "ope":"soma"})
         if "ERRO" not in r1.text:
             self.fail("Enviei um b inválido, esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     def test_06_incompleto(self):
         r1 = requests.get("http://localhost:5000/resultado",params={"b":20, "ope":"sub"})
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava a) e esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     
     def test_07_b_incompleto(self):
         print("parazzi")
         r1 = requests.get("http://localhost:5000/resultado",params={"a":20, "ope":"sub"})
         print("tamanho",len(r1.text.split("ERRO")))
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava a) e esperava que a resposta tivesse a string 'ERRO'")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")

     def test_08_ope_incompleto(self):
         r1 = requests.get("http://localhost:5000/resultado",params={"a":20, "b":10})
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava ope) e esperava que a resposta tivesse a string 'ERRO'")     
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     
     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()