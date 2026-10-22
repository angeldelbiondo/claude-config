import re, unicodedata
# ponytail: palabras clave, no semántica. Si falla seguido, subir a embeddings (pendiente "búsqueda semántica" del vault).
INTENCIONES = {
  "depurar":   r"\berror|no funciona|no (arranca|carga|abre|sirve|anda)|se (me )?(bloque|congel|cuelg|cay|traba)|microcongel|lent[oa]\b|falla|crash|bug|no (lo )?detecta|por que (pasa|se|no)",
  "diseno":    r"\bui\b|interfaz|pantalla|landing|disen|se ve (feo|mal|generic)|colores|tipografi|animaci|gsap|layout|frontend|diagrama|estilo visual",
  "investigar":r"investig|busca|reddit|youtube\.com|youtu\.be|tiktok|que dice la gente|foros?\b|competen|mercado|github\.com/|repos?\b|articulo|video",
  "decidir":   r"buena idea|vale la pena|que (propones|opinas|concluyes|recomiendas)|critic|contras|abogado del diablo|conclu|deberia|conviene",
  "construir": r"implementa|\bcrea\b|crear|haz un (script|bot|app)|agrega|construi|mvp|funcionalidad|\bconectal[oa]|conecta (el|la|los|con)\b",
  "revisar":   r"revisa|seguridad|over-?engineer|sobre-?ingenier|testing|\btest|asegura (que|la)|verifica|chequea",
  "recordar":  r"guarda|salva|no quiero perder|anota|vault|obsidian|retom|que teniamos|en mis notas",
  "escribir":  r"documento|informe|propuesta|presentaci|\bppt|word\b|\bpdf\b|correo|email|readme|\bcopy\b",
  "datos":     r"excel|\bcsv\b|\bsql\b|\bgraficos?\b|dashboard|power ?bi|\.pbix|estadistic|backtest|sharpe",
}
PAT = {k: re.compile(v) for k, v in INTENCIONES.items()}

def norm(s):
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()

def ruta(prompt):
    p = norm(prompt)
    hits = [k for k, rx in PAT.items() if rx.search(p)]
    if not hits: return ""
    if len(hits) > 2: return "[ruta] Pedido con varias intenciones (" + ", ".join(hits) + "): usar la skill `orquestar` y mostrar el plan antes."
    return "[ruta] Intención probable: " + " + ".join(f"`{h}`" for h in hits) + (". Si son dos, `orquestar` muestra el plan." if len(hits) == 2 else ". Cargarla si aplica; si no, ignorar.")

if __name__ == "__main__":
    assert "depurar" in ruta("POR QUE SE ME bloqueo y no puedo poner manualmente mi grafica externa")
    assert "depurar" in ruta("se me microcongela cada x segundos")
    assert "investigar" in ruta("okay , ahora este https://www.youtube.com/watch?v=2oXhVue6ajE")
    assert "decidir" in ruta("osea que concluyes de ambos videos, no hay nada valioso")
    assert "recordar" in ruta("guarda esto en el vault")
    assert ruta("dale, haz eso, me gusta tu proactividad.") == ""
    assert ruta("sigue con lo que estabas haciendo") == ""
    assert "datos" not in ruta("no puedo poner manualmente mi grafica externa")  # gráfica = GPU en Panamá
    assert ruta("tengo conectado el cable ethernet pero no lo detecta").count("depurar") and "construir" not in ruta("tengo conectado el cable ethernet pero no lo detecta")
    assert "datos" in ruta("hazme un grafico de las ventas")
    print("ok")
