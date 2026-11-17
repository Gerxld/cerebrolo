import os
import requests
import numpy as np

OLLAMA_URL = "http://localhost:11434"
MODELO_EMBEDDING = "nomic-embed-text"
MODELO_LLM = "qwen2.5:3b"
CARPETA_DOCUMENTOS = "documentos"


def cargar_documentos(carpeta):
    documentos = []
    for nombre in os.listdir(carpeta):
        if nombre.endswith(".txt"):
            ruta = os.path.join(carpeta, nombre)
            with open(ruta, "r", encoding="utf-8") as f:
                documentos.append({
                    "fuente": nombre,
                    "texto": f.read()
                })
    return documentos


def crear_chunks(documentos, tamano=220, solapamiento=40):
    chunks = []
    for doc in documentos:
        texto = doc["texto"].strip()
        inicio = 0
        while inicio < len(texto):
            fin = inicio + tamano
            fragmento = texto[inicio:fin].strip()
            if fragmento:
                chunks.append({
                    "fuente": doc["fuente"],
                    "texto": fragmento
                })
            inicio += tamano - solapamiento
    return chunks


def embedding(texto):
    respuesta = requests.post(
        f"{OLLAMA_URL}/api/embed",
        json={"model": MODELO_EMBEDDING, "input": texto},
        timeout=120
    )
    respuesta.raise_for_status()
    return np.array(respuesta.json()["embeddings"][0], dtype=float)


def similitud_coseno(a, b):
    denominador = np.linalg.norm(a) * np.linalg.norm(b)
    if denominador == 0:
        return 0.0
    return float(np.dot(a, b) / denominador)


def indexar(chunks):
    indice = []
    for chunk in chunks:
        indice.append({
            "fuente": chunk["fuente"],
            "texto": chunk["texto"],
            "vector": embedding(chunk["texto"])
        })
    return indice


def recuperar(pregunta, indice, k=3):
    vector_pregunta = embedding(pregunta)
    resultados = []

    for item in indice:
        score = similitud_coseno(vector_pregunta, item["vector"])
        resultados.append({**item, "score": score})

    resultados.sort(key=lambda x: x["score"], reverse=True)
    return resultados[:k]


def mostrar_recuperados(resultados):
    print("\n--- CHUNKS RECUPERADOS ---")
    for i, item in enumerate(resultados, 1):
        print(f"{i}. {item['fuente']} | similitud={item['score']:.3f}")
        print(item["texto"])
        print()


def construir_prompt(pregunta, resultados):
    contexto = "\n\n".join(
        f"Fuente: {r['fuente']}\n{r['texto']}"
        for r in resultados
    )
    return f"""
Responde únicamente usando el CONTEXTO proporcionado.
Si el contexto no contiene información suficiente para responder, indica exactamente:
"No encuentro esa información en los documentos proporcionados."

Incluye al final las fuentes utilizadas.
CONTEXTO:
{contexto}

PREGUNTA:
{pregunta}
"""


def generar_respuesta(prompt):
    respuesta = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODELO_LLM,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )
    respuesta.raise_for_status()
    return respuesta.json()["response"]


def preguntar(pregunta, indice):
    resultados = recuperar(pregunta, indice, k=3)
    mostrar_recuperados(resultados)

    prompt = construir_prompt(pregunta, resultados)
    respuesta = generar_respuesta(prompt)

    print("--- RESPUESTA RAG ---")
    print(respuesta)


if __name__ == "__main__":
    documentos = cargar_documentos(CARPETA_DOCUMENTOS)
    chunks = crear_chunks(documentos)

    print(f"Documentos cargados: {len(documentos)}")
    print(f"Chunks creados: {len(chunks)}")
    print("Generando índice vectorial...")

    indice = indexar(chunks)

    while True:
        pregunta = input("\nPregunta (o 'salir'): ").strip()
        if pregunta.lower() == "salir":
            break
        preguntar(pregunta, indice)
