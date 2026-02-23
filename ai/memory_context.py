from collections import defaultdict

history = defaultdict(list)

def add_message(user_id, role, text):
    history[user_id].append((role, text))

    # mantém só últimas mensagens
    history[user_id] = history[user_id][-6:]

def get_context(user_id):
    return history[user_id]
