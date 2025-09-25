import re
from .emoji_map import EMOJI_MAP

def emojify_text(text: str, emoji_map: dict = None):
    """
    Replaces known words with emojis in the given text.
    """
    if emoji_map is None:
        print("Using Default Map")
        emoji_map = EMOJI_MAP

    def replace_word(match):
        word = match.group(0).lower()
        return emoji_map.get(word, word)

    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in emoji_map.keys()) + r')\b', flags=re.IGNORECASE)
    return pattern.sub(replace_word, text)
