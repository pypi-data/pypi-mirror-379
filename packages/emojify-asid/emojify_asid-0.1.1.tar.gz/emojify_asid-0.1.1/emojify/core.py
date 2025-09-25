import re
from .emoji_map import EMOJI_MAP

def emojify_text(text: str):
    """
    Replaces known words with emojis in the given text.
    """
    def replace_word(match):
        word = match.group(0).lower()
        return EMOJI_MAP.get(word, word)

    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in EMOJI_MAP.keys()) + r')\b', flags=re.IGNORECASE)
    return pattern.sub(replace_word, text)
