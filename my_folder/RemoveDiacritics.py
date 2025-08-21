import re

def remove_diacritics(text: str) -> str:
    """
    Removes Arabic diacritics (Tashdid, Fatha, Damma, etc.) and Tatwil/Kashida from the input Persian text.

    Parameters:
        text (str): The input text to clean.

    Returns:
        str: The cleaned text without diacritics.
    """
    arabic_diacritics = re.compile("""
        ّ |  # Tashdid
        َ |  # Fatha
        ً |  # Tanwin Fath
        ُ |  # Damma
        ٌ |  # Tanwin Damm
        ِ |  # Kasra
        ٍ |  # Tanwin Kasr
        ْ |  # Sukun
        ـ    # Tatwil/Kashida
    """, re.VERBOSE)

    cleaned_text = re.sub(arabic_diacritics, '', text)
    return cleaned_text

# ----------- مثال استفاده -----------
sample_text = "مُحَمَّد دارد می‌آید و کِتاب را می‌خوانَد"
cleaned = remove_diacritics(sample_text)
print("متن بدون دیاکریت:", cleaned)

