"""Paso 24: fuerza la segunda salida del loop (max_iteraciones) con un limite bajo."""
import agente_proyecto as ap

if __name__ == "__main__":
    objetivo = input("Objetivo para el agente: ").strip()
    resultado = ap.ejecutar_agente(objetivo, max_iteraciones=2)
    print("\nValor devuelto por ejecutar_agente:", repr(resultado))
