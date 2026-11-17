import unittest
from tasks import agregar_tarea, completar_tarea, pendientes, buscar_tareas, ordenar_por_prioridad

class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer capítulo", "alta")
        self.assertEqual(tarea["titulo"], "Leer capítulo")
        self.assertEqual(tarea["prioridad"], "alta")
        self.assertFalse(tarea["completada"])

    def test_prioridades_validas(self):
        tareas = []
        for prioridad in ("alta", "media", "baja"):
            tarea = agregar_tarea(tareas, "Tarea", prioridad)
            self.assertEqual(tarea["prioridad"], prioridad)

    def test_prioridad_invalida(self):
        tareas = []
        for prioridad in ("urgente", "", None, "ALTA"):
            with self.assertRaises(ValueError):
                agregar_tarea(tareas, "Tarea", prioridad)
        self.assertEqual(tareas, [])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "baja")
        completar_tarea(tareas, 1)
        self.assertEqual(len(pendientes(tareas)), 0)

    def test_pendientes_excluye_completadas(self):
        tareas = []
        agregar_tarea(tareas, "A", "alta")
        agregar_tarea(tareas, "B", "media")
        completar_tarea(tareas, 1)
        self.assertEqual([t["titulo"] for t in pendientes(tareas)], ["B"])

    def test_buscar_tareas_ignora_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Leer Capítulo", "alta")
        agregar_tarea(tareas, "Practicar", "baja")
        self.assertEqual([t["titulo"] for t in buscar_tareas(tareas, "LEER")], ["Leer Capítulo"])
        self.assertEqual([t["titulo"] for t in buscar_tareas(tareas, "capítulo")], ["Leer Capítulo"])

    def test_buscar_tareas_sin_coincidencias(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "baja")
        self.assertEqual(buscar_tareas(tareas, "xyz"), [])

    def test_buscar_texto_inexistente_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "baja")
        agregar_tarea(tareas, "Leer capítulo", "alta")
        self.assertEqual(buscar_tareas(tareas, "inexistente"), [])

    def test_buscar_texto_vacio_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "baja")
        self.assertEqual(buscar_tareas(tareas, ""), [])

    def test_ordenar_por_prioridad_orden_correcto(self):
        tareas = []
        agregar_tarea(tareas, "A", "baja")
        agregar_tarea(tareas, "B", "alta")
        agregar_tarea(tareas, "C", "media")
        self.assertEqual([t["titulo"] for t in ordenar_por_prioridad(tareas)], ["B", "C", "A"])

    def test_ordenar_por_prioridad_estable(self):
        tareas = []
        agregar_tarea(tareas, "A", "media")
        agregar_tarea(tareas, "B", "alta")
        agregar_tarea(tareas, "C", "media")
        agregar_tarea(tareas, "D", "alta")
        self.assertEqual([t["titulo"] for t in ordenar_por_prioridad(tareas)], ["B", "D", "A", "C"])

    def test_ordenar_por_prioridad_no_modifica_original(self):
        tareas = []
        agregar_tarea(tareas, "A", "baja")
        agregar_tarea(tareas, "B", "alta")
        copia = [dict(t) for t in tareas]
        resultado = ordenar_por_prioridad(tareas)
        self.assertIsNot(resultado, tareas)
        self.assertEqual(tareas, copia)
        self.assertEqual([t["titulo"] for t in tareas], ["A", "B"])

    def test_ordenar_por_prioridad_lista_vacia(self):
        self.assertEqual(ordenar_por_prioridad([]), [])

if __name__ == "__main__":
    unittest.main()
