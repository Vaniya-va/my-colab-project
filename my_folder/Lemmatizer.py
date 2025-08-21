
from hazm import Lemmatizer, word_tokenize

# Initialize the Hazm Lemmatizer
lemmatizer = Lemmatizer()

def lemmatize_text(text: str) -> list:
    """
    Tokenizes and lemmatizes a Persian text using Hazm.

    Parameters:
        text (str): The Persian input text.

    Returns:
        list: A list of lemmatized tokens.
    """
    tokens = word_tokenize(text)
    return [lemmatizer.lemmatize(token) for token in tokens]


# --- نمونه استفاده ---
text = "کتاب‌هایم را خوانده‌ام و دوست داشتم"
lemmatized_tokens = lemmatize_text(text)
print(lemmatized_tokens)
