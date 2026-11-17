from pathlib import Path
from ollama import chat

MODELO = 'qwen3:4b'


def resumir_vulnerable(texto):
    prompt = f'''Eres un analista de soporte.
Resume el contenido recibido en máximo 3 líneas.

CONTENIDO:
{texto}
'''
    r = chat(model=MODELO, messages=[{'role': 'user', 'content': prompt}], think=False)
    return r.message.content


if __name__ == '__main__':
    for nombre in ['ticket_normal.txt', 'ticket_inyectado.txt']:
        texto = Path('documentos', nombre).read_text(encoding='utf-8')
        print(f'\n--- {nombre} ---')
        print(resumir_vulnerable(texto))
