from hazm import word_tokenize

# لیست نمونه stopwords فارسی
persian_stopwords = {
    "و", "به", "در", "از", "که", "با", "این", "را", "برای", "است", "می", "شد", "آن", "تا", "هم"
}

def remove_stopwords_from_text(text: str) -> list:
    """
    توکنایز کردن متن و حذف stopwords فارسی.

    Args:
        text (str): متن فارسی ورودی.

    Returns:
        list: لیست توکن‌ها بدون stopwords.
    """
    tokens = word_tokenize(text)
    return [token for token in tokens if token not in persian_stopwords]

# --- نمونه استفاده ---
text = "من میخوام برم سینما ولی نمیتونم"
tokens = remove_stopwords_from_text(text)
print(tokens)
# خروجی: ['میخوام', 'برم', 'سینما', 'نمیتونم']
