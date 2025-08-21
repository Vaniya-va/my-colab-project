import string

def remove_punctuations(text: str) -> str:
    """
    Removes both standard English and Persian punctuations from the input text.

    Parameters:
        text (str): The input text to clean.

    Returns:
        str: The text after removing all specified punctuations.
    """
    persian_punctuations = '''`÷×؛#<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    punctuations_list = string.punctuation + persian_punctuations
    translator = str.maketrans('', '', punctuations_list)
    cleaned_text = text.translate(translator)
    return cleaned_text

# ----------- مثال استفاده -----------
sample_text = "سلام! این یک متن، نمونه است. آیا آماده‌ای؟"
cleaned = remove_punctuations(sample_text)
print("متن بدون علامت نگارشی:", cleaned)

