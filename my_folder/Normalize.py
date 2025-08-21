import re
import hazm

def normalize_arabic(text: str) -> str:
    """
    Normalizes Arabic characters to their Persian equivalents.
    """
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ي", "ی", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ی", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("ك", "ک", text)
    return text

def remove_html_tags(text: str) -> str:
    return re.sub(r'<[^>]+>', '', text)

def remove_urls(text: str) -> str:
    return re.sub(r'https?://\S+|www\.\S+', '', text)

def remove_emojis(text: str) -> str:
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002700-\U000027BF"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_numbers(text: str) -> str:
    return re.sub(r'[0-9۰-۹]', '', text)

def handle_special_characters(text: str) -> str:
    return re.sub(r'[^\w\s]', ' ', text)

def remove_diacritics(text: str) -> str:
    arabic_diacritics = re.compile(r"[ّ َ ً ُ ٌ ِ ٍ ْ ـ]", re.VERBOSE)
    return re.sub(arabic_diacritics, '', text)

def remove_repeating_chars(text: str) -> str:
    return re.sub(r'(.)\1+', r'\1', text)

def normalize_text(text: str) -> str:
    """
    Normalizes Persian text:
    - Removes HTML, URLs, emojis, numbers
    - Handles special characters
    - Normalizes Arabic characters
    - Removes diacritics
    - Removes repeating letters
    - Applies Hazm normalization
    """
    text = remove_html_tags(text)
    text = remove_urls(text)
    text = remove_emojis(text)
    text = remove_numbers(text)
    text = handle_special_characters(text)
    text = normalize_arabic(text)
    text = remove_diacritics(text)
    text = remove_repeating_chars(text)
    normalizer = hazm.Normalizer()
    text = normalizer.normalize(text)
    return text

# --- مثال استفاده ---
sample_text = "می‌خواااااام برم سینماااا! 😍 http://test.com"
normalized = normalize_text(sample_text)
print(normalized)

