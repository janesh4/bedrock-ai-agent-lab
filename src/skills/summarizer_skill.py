def summarize_text(text, limit=150):

    if len(text) <= limit:
        return text

    return text[:limit] + "..."
