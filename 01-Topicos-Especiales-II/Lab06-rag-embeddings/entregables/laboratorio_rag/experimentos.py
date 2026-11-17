"""Experimentos de los pasos 25 y 26 y del reto (27).
Reutiliza las funciones de rag_universidad.py sin modificarlas.
Uso: python -u experimentos.py "<pregunta>" [tamano] [k]
"""
import sys
import rag_universidad as rag

pregunta = sys.argv[1]
tamano = int(sys.argv[2]) if len(sys.argv) > 2 else 220
k = int(sys.argv[3]) if len(sys.argv) > 3 else 3

documentos = rag.cargar_documentos(rag.CARPETA_DOCUMENTOS)
chunks = rag.crear_chunks(documentos, tamano=tamano)
print(f"Documentos cargados: {len(documentos)}")
print(f"Tamano de chunk: {tamano} | solapamiento: 40 | k: {k}")
print(f"Chunks creados: {len(chunks)}")
print("Generando índice vectorial...")
indice = rag.indexar(chunks)

print(f"\nPregunta: {pregunta}")
resultados = rag.recuperar(pregunta, indice, k=k)
rag.mostrar_recuperados(resultados)
prompt = rag.construir_prompt(pregunta, resultados)
respuesta = rag.generar_respuesta(prompt)
print("--- RESPUESTA RAG ---")
print(respuesta)
