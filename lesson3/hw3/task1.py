"""
Записати в стрічку філософію Пайтона
- Знайти в заданій стрічці кількість
  входжень слів (better, never, is)
- Вивести весь текст у верхньому регістрі (всі великі літери)
- Замінити всі входження символу “і” на “&”
"""

PYTHON_PHILOSOPHY_TEXT = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

def count_key_words(key_words_dict: dict):
    better_word_counter = int(PYTHON_PHILOSOPHY_TEXT.count(key_words_dict['better']))
    never_word_counter = int(PYTHON_PHILOSOPHY_TEXT.count(key_words_dict['never']))
    is_word_counter = int(PYTHON_PHILOSOPHY_TEXT.count(key_words_dict['is']))

    print("Word %s -> %d times  in text." % (key_words_dict['better'], better_word_counter))
    print("Word {key}  -> {counter} times  in text.".format(key=key_words_dict['never'], counter=never_word_counter))
    print(f"Word {key_words_dict['is']}     -> {is_word_counter} times in text.")

def upper_text():
    print(PYTHON_PHILOSOPHY_TEXT.upper())

def replace_symbol(changed_symbol: str, chang_symbol: str):
    print(PYTHON_PHILOSOPHY_TEXT.replace(changed_symbol, chang_symbol))

if __name__ == '__main__':
    SEARCH_KEY_WORDS = {
        'better': 'better',
        'never': 'never',
        'is': 'is',
    }

    # Count current input words
    count_key_words(key_words_dict=SEARCH_KEY_WORDS)

    # Set input text to uppercase
    upper_text()

    # Replace @changed_symbol with @chang_symbol
    replace_symbol(changed_symbol='i', chang_symbol='&')
