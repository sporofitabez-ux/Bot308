from ai.intent import detect_intent
from ai.memory_context import add_message
from services.anilist import search_manga

async def process_ai(user_id, text):

    add_message(user_id, "user", text)

    intent = detect_intent(text)

    # RECOMENDAÇÃO SIMPLES
    if intent == "recommend":
        reply = (
            "Hmm 👀 se quer algo bom, tenta:\n"
            "🔥 Solo Leveling\n"
            "⚔️ Omniscient Reader\n"
            "🩸 Tokyo Ghoul"
        )
        return reply, None

    # BUSCA DIRETA
    if intent in ["search", "similar"]:
        manga = await search_manga(text)

        if manga:
            title = manga["title"]["romaji"]
            desc = manga["description"][:400]
            genres = ", ".join(manga["genres"])
            cover = manga["coverImage"]["large"]

            reply = f"""
📖 {title}

🧾 {desc}

🎭 {genres}
"""
            return reply, cover

    # CONVERSA NORMAL
    return (
        "Conta mais 😄\n"
        "Você prefere algo dark, romance ou ação?"
    ), None
