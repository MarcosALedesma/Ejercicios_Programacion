from deep_translator import GoogleTranslator

def traductora(texto, origen='en', destino='es'):
 
    if not texto:
        return ''
    try:
        traductor = GoogleTranslator(source=origen, target=destino)
        return traductor.translate(texto)
    except Exception as e:
        print(f"Error traduciendo: {e}")
    return texto  
