import unittest

import tareas


class TestTareas(unittest.TestCase):
    def setUp(self):
        self.lista = []

    def test_agregar_tarea_valida(self):
        tarea = tareas.agregar_tarea(self.lista, "  Leer  ", " ALTA ")

        self.assertEqual(len(self.lista), 1)
        self.assertIs(self.lista[0], tarea)
        self.assertEqual(tarea["titulo"], "Leer")
        self.assertEqual(tarea["prioridad"], "alta")
        self.assertFalse(tarea["completada"])

    def test_rechazar_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            tareas.agregar_tarea(self.lista, "Leer", "urgente")

        self.assertEqual(self.lista, [])

    def test_rechazar_titulo_vacio(self):
        with self.assertRaises(ValueError):
            tareas.agregar_tarea(self.lista, "   ", "media")

        self.assertEqual(self.lista, [])

    def test_marcar_tarea_como_completada(self):
        tareas.agregar_tarea(self.lista, "Leer", "baja")
        tareas.agregar_tarea(self.lista, "Escribir", "media")

        tareas.completar_tarea(self.lista, 2)

        self.assertFalse(self.lista[0]["completada"])
        self.assertTrue(self.lista[1]["completada"])

    def test_completar_tarea_inexistente(self):
        tareas.agregar_tarea(self.lista, "Leer", "baja")

        with self.assertRaises(ValueError):
            tareas.completar_tarea(self.lista, 5)

        self.assertFalse(self.lista[0]["completada"])

    def test_completar_tarea_con_cero(self):
        tareas.agregar_tarea(self.lista, "Leer", "baja")
        tareas.agregar_tarea(self.lista, "Escribir", "media")

        with self.assertRaises(ValueError):
            tareas.completar_tarea(self.lista, 0)

        self.assertFalse(self.lista[0]["completada"])
        self.assertFalse(self.lista[1]["completada"])

    def test_completar_tarea_con_numero_negativo(self):
        tareas.agregar_tarea(self.lista, "Leer", "baja")
        tareas.agregar_tarea(self.lista, "Escribir", "media")

        with self.assertRaises(ValueError):
            tareas.completar_tarea(self.lista, -1)

        self.assertFalse(self.lista[0]["completada"])
        self.assertFalse(self.lista[1]["completada"])


if __name__ == "__main__":
    unittest.main()
