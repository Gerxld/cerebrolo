import unittest
from calculadora import dividir, promedio, porcentaje, mediana


class TestCalculadora(unittest.TestCase):

    # Casos normales (propuestos por el modelo)
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(8, 4), 2)
        self.assertEqual(dividir(15, 3), 5)

    def test_promedio_con_muchos_elementos(self):
        self.assertEqual(promedio([1, 2, 3, 4, 5]), 3)

    def test_porcentaje_normal(self):
        self.assertEqual(porcentaje(5, 100), 5)

    # Casos límite
    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_promedio_lista_vacia(self):
        # El modelo propuso assertEqual(promedio([]), 0); se corrigió a ValueError
        # porque el enunciado pidió excepciones claras y 0 sería un promedio falso.
        with self.assertRaises(ValueError):
            promedio([])

    def test_porcentaje_cero_total(self):
        with self.assertRaises(ValueError):
            porcentaje(10, 0)


class TestMediana(unittest.TestCase):
    # Pruebas propuestas por el modelo (paso 23), copiadas tal cual
    def test_mediana_cantidad_impar(self):
        self.assertEqual(mediana([3, 1, 4, 1, 5]), 3)
        self.assertEqual(mediana([10, 20, 30, 40, 50]), 30)
        self.assertEqual(mediana([-5, -2, 0, 2, 5]), 0)

    def test_mediana_cantidad_par(self):
        self.assertEqual(mediana([1, 3, 5, 7]), 4)
        self.assertEqual(mediana([10, 20, 30, 40]), 25)
        # El modelo esperaba -3; corregido a mano: ordenada es [-7, -5, -3, -1] y (-5 + -3) / 2 = -4
        self.assertEqual(mediana([-1, -3, -5, -7]), -4)

    def test_mediana_cantidad_par_2(self):
        self.assertEqual(mediana([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(mediana([10, 20, 30, 40, 50, 60]), 35)

    def test_mediana_vacia(self):
        with self.assertRaises(ValueError):
            mediana([])

    # Agregada a mano: el modelo no probó que la lista de entrada quede intacta
    def test_mediana_no_modifica_la_lista(self):
        datos = [5, 1, 4]
        mediana(datos)
        self.assertEqual(datos, [5, 1, 4])


if __name__ == '__main__':
    unittest.main()
