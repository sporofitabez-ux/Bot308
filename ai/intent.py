def detect_intent(text: str):

    text = text.lower()

    if "recomenda" in text or "sugere" in text:
        return "recommend"

    if "parecido" in text or "tipo" in text:
        return "similar"

    if len(text.split()) <= 3:
        return "search"

    return "chat"
