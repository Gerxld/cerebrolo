import unittest
from usuarios import email_valido, crear_usuario

class TestUsuarios(unittest.TestCase):
    def test_email_valido(self):
        self.assertTrue(email_valido("ana@utp.ac.pa"))

    def test_email_invalido(self):
        self.assertFalse(email_valido("ana@utp"))

    def test_nombre_obligatorio(self):
        with self.assertRaises(ValueError):
            crear_usuario("", "ana@utp.ac.pa")

if __name__ == "__main__":
    unittest.main()
