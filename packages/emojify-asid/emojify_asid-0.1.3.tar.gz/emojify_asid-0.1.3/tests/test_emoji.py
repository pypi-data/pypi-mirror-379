from emojify import emojify_text

def test_basic():
    text = "I love my cat and my computer"
    result = emojify_text(text)
    return result

if __name__ == '__main__':
    print(test_basic())